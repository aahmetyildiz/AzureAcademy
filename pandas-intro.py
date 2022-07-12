import pandas as pd

csv = pd.read_csv("Expenses.csv")


def show_first(row_count):
    result = csv.head(row_count)
    return result

def show_last(row_count):
    result = csv.tail(row_count)
    return result

def adidas():
    result = csv.loc[csv['Merchant'] == 'Adidas']
    return result

def nike_or_adidas():
    result = csv.loc[(csv['Merchant'] == 'Adidas') | (csv['Merchant'] == 'Nike') ]
    return result


def q_merchant(merchant_list):
    result = pd.DataFrame()
    for merchant in merchant_list:
        #result = result.append(csv.loc[csv['Merchant'] == merchant])
        result = pd.concat([result, csv.loc[csv['Merchant'] == merchant]])

    return result

def q_price(min=0, max=999999):
    data = csv
    data['Price'] = data['Price'].str[1:].astype(float)
    result = data.loc[(data['Price'] >= min) & (data['Price'] <= max)]

    return result



#print(show_first(5))
#print(show_last(5))
#print(adidas())
#print(nike_or_adidas())

#print(q_merchant(['Adidas', 'Nike']))

print(q_price(50, 80))




