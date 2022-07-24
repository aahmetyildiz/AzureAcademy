import requests
import json





class RandomUser:
    def __init__(self, user_count):
        self.url = f'https://randomuser.me/api/?results={user_count}'

    def getAll(self):
        r = requests.get(self.url)
        r_json = r.json()

        return r_json['results']

    def fields(self, json):
        data = {
            'gender' : json['gender'],
            'nat' : json['nat'],
            'picture': json['picture']['large']
        }
        return data


    def multiple_users(self):
        user_list_json = self.getAll()
        result_user_list = []

        for user in user_list_json:
            print(self.fields(user))





#class RandomUser(User count [integer])
users = RandomUser(100)

#Get all user
#user_list = users.getAll()


user_list = users.multiple_users()

"""
for user in user_list:
    print(user)
"""



