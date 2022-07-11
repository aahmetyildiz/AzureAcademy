# Import Request package
import requests

# Import Beautiful Soup in your file
from bs4 import BeautifulSoup


class Page:
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)

    def get_html(self):
        return self.page.text

    def get_bs(self):
        return BeautifulSoup(self.page.text, 'html.parser')


"""
#google_html = Page("https://www.ah.nl/producten/").get_html()

google_bs = Page("https://www.bbc.com").get_bs()
#print(google_bs)

h3_list = google_bs.find_all("h3", class_="media__title")

#print(a_list)

for h3 in h3_list:
    print(h3.find('a')['href'])
    print(h3.find('a').get_text(strip=True))
    print('')

"""

