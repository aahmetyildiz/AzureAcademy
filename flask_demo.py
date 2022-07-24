# import modules
import flask
from flask import request, jsonify
import requests
import pandas as pd
import json

# Init app
app = flask.Flask(__name__)
app.config["DEBUG"] = True


def get_elements():
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    r = requests.get(url)
    json_data = r.json()
    return json_data

data = get_elements()['elements']



# put endpoints
@app.route('/api/players', methods=['GET'])
def players():

    df_data = pd.DataFrame(data).filter(['first_name', 'second_name','team', 'total_points', 'in_dreamteam'])
    if request.args.get('dream_team') is not None:
        dream_team = request.args.get('dream_team')
        if dream_team == "false":
            df_data = df_data.loc[df_data['in_dreamteam'] == False]

        if dream_team == "true":
            df_data = df_data.loc[df_data['in_dreamteam'] == True]


    if request.args.get('min_tp') is not None:
        min_tp = request.args.get('min_tp')

        if min_tp.isnumeric() == True:
            df_data = df_data.loc[df_data['total_points'] >= float(min_tp)]


    result = df_data.to_json(orient="index")
    return jsonify(json.loads(result))





# Run App
app.run()