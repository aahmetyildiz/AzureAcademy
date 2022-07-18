from web_scraping import Page
from bs4 import BeautifulSoup



class Weather:
    def __init__(self, city, days):
        self.city = city
        self.days = days
        self.url = 'https://www.bbc.com/weather/'+city
        self.requested_page = Page(self.url).get_html()

        # Store the Beautiful Soup of the page in the self.page
        self.page = Page(self.url).get_bs()


    # Add get_weather method
    def get_weather(self):
        """
        Takes as parameter the max number of days (between 1 and 6).

        Should return an array of dictonaries per day with the day of the week, weather type
        max. degrees celcius and min. degrees celcius.
        """
        weather_bs = Page(self.url).get_bs()
        weather_data = weather_bs.find_all("li", class_="wr-day")
        # Add your Beautiful Soup code here to extract all the necessary data

        return weather_data

    # Your print function
    def print_weather(self):
        """
        This function takes the data of a single day, and prints a string that includes the
        day of the week, the weather type, max. degrees celcius and min. degrees celcius
        """

        # Add your print statement here

        return ""





def main():
    location = int(input("Select location for weather data (pick a number) \n 1) Amsterdam \n 2) Groningen \n 3) Rotterdam \n Your answer:  "))
    location -=1
    # Match the given number with the corresponding city
    cities = [["Amsterdam", "2759794"], ["Groningen", "2755251"], ["Rotterdam", "1"]]
    city = cities[location][1]

    print(f"You have selected {cities[location][0]}")

    #number_of_days = int(input("Select the max number of days (between 1 and 6) of which you want to get the weather data."))
    #print(f"You have selected: {number_of_days} day(s)")
    days = 4
    # Initialization of the Weather class
    #print(Weather(city, days).get_weather())


    # call the get_weather method on the weather variable that you just created
    weather_data = Weather(city, days).get_weather()
    #print(weather_data)




    print("We have found the following data:")

    # Loop trough the get_weather data


    for day in weather_data:
        # Call your print method of the Weather class
        print(day.find('div', attrs={'class':'wr-day__title'})['aria-label'])




main()