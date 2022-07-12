import pandas as pd

class Expenses:
    def __init__(self, path):
        """
        This function takes in the path of the excel-file and loads the file into the pandas,
        which is stored in the self.csv
        """

        self.csv = pd.read_csv(path)

    def get_csv(self):
        """
        This function prints out the csv
        """

        print(self.csv)
        return self

    def clean(self):
        """
        This function calls all the private functions, to clean up the data
        """

        self.__clean_prices()
        self.__remove_na()
        self.__seperate_date_time()
        return self

    def __remove_na(self):
        # Find out how to Remove empty values and store the result in self.csv
        self.csv = self.csv.dropna() #OK >> Add method here

        # The return statement is correct, don't touch it :)
        return self

    def __clean_prices(self):
        # Find out how to remove the € sign from a string
        self.csv['Price'] = self.csv['Price'].str.strip("€")

        # Find out how to replace some character in the string, in this case the dot with the comma
        #self.csv['Price'] = self.csv['Price'].str.replace('.',',') #OK >> Add method

        # Find out how to convert a string to a float
        self.csv['Price'] = self.csv['Price'].astype(float) #OK >>  Add method

        # The return statement is correct, don't touch it :)
        return self

    def __seperate_date_time(self):
        # Seperate the time from the date and store date and time seperately
        self.csv['Time'] = self.csv['Date'].str.split(" ", n=1, expand=True)[0] #OK >> Add method
        self.csv['Date'] = self.csv['Date'].str.split(" ", n=1, expand=True)[1] #OK >> Add method

        # The return statement is correct, don't touch it :)
        return self

    def get_average_expense(self):
        # Get average expense based on the price column, and round it
        return self.csv['Price'].mean().__round__()

    def get_highest_expense(self):
        highest_value = 0
        dictionary = None

        for expense in self.csv.values:
            current_price = expense[3]
            if current_price > highest_value:
                highest_value = current_price
                dictionary = {
                    "Date": expense[0],
                    "Time": expense[4],
                    "Category": expense[1],
                    "Merchant": expense[2],
                    "Price":  expense[3],
                }
                #dictionary = {"Expense_category": expense[1], "Price": current_price}

        return highest_value, dictionary

    def get_lowest_expense(self):
        #OK>> You can use most of the code of the get_highest_expense method. Return lowest value and the dictionary
        lowest_value = 999999
        dictionary = None

        for expense in self.csv.values:
            current_price = expense[3]
            if current_price < lowest_value:
                lowest_value = current_price
                dictionary = {
                    "Date": expense[0],
                    "Time": expense[4],
                    "Category": expense[1],
                    "Merchant": expense[2],
                    "Price": expense[3],
                }

        return lowest_value, dictionary


    def filter(self, min=50, max=100):
        #OK>> Use a method that returns only the rows with a price smaller than 50 and bigger than 100

        return self.csv.loc[(self.csv['Price'] >= min) & (self.csv['Price'] <= max)]

    def column_order(self):
        self.csv = self.csv.reindex(columns=['Date', 'Time', 'Category', 'Merchant', 'Price'])
        return self


data = Expenses('Expenses.csv')

#result = data.get_csv()
#result = data.clean().get_csv()
result = data.clean().get_average_expense()
#result = data.clean().get_highest_expense()
#result = data.clean().get_lowest_expense()
#result = data.clean().filter()

#result = data.clean().column_order().filter(50, 180)


print(result)


