from web_scraping import Page


class Bookstore:
    def __init__(self, start_page=1, last_page=-1):
        self.page = start_page
        self.last_page = last_page
        self.url = "http://books.toscrape.com/"
        self.star_list = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

    def scrapdata(self, blok):
        url = blok.a['href']
        name = blok.h3.a['title']
        price_raw = blok.find('p', attrs={'class': 'price_color'}).get_text()
        price = float(price_raw[2:])
        star_raw = blok.p['class'][1]
        star = self.star_list[star_raw]

        data = {
            'name': name,
            'price': price,
            'url': url,
            'star': star,
            'note':'',
        }
        return data

    def getAll(self):
        self.result_list=[]
        while (True):
            books_bs = Page("http://books.toscrape.com/catalogue/page-" + str(self.page) + ".html").get_bs()
            books_bloks = books_bs.find_all("article", class_="product_pod")

            for book in books_bloks:
                self.result_list.append(self.scrapdata(book))

            next_page_ctrl = books_bs.find_all("li", class_="next")

            if len(next_page_ctrl) == 1 and (self.page <= self.last_page or self.last_page == -1):
                self.page += 1
            else:
                break

        return self.result_list

    def priceFilter(self, min=0, max=99999):
        self.price_result_list=[]
        self.book_list = self.getAll()
        self.p_min = min
        self.p_max = max

        #Is Minumum price less than maximum price control
        if self.p_min > self.p_max:
            self.p_min = max
            self.p_max = min

        for book in self.book_list:
            if book['price'] >= self.p_min and book['price'] <= self.p_max:
                self.price_result_list.append(book)

        return self.price_result_list

    def starFilter(self, min=0, max=5):
        self.star_result_list=[]
        self.book_list = self.getAll()
        self.s_min = min
        self.s_max = max

        #Is Minumum star less than maximum star control
        if self.s_min > self.s_max:
            self.s_min = max
            self.s_max = min

        for book in self.book_list:
            if book['star'] >= self.s_min and book['star'] <= self.s_max:
                self.star_result_list.append(book)

        return self.star_result_list

    def searchName(self, text):
        if len(text) >= 3 or text is None:
            self.search_result_list = []
            self.book_list = self.getAll()

            for book in self.book_list:
                if book['name'].find(text) >= 0:
                    self.search_result_list.append(book)

        else:
            self.search_result_list = ['WARNING: Serch text must be minumum 3 charachter!']

        return self.search_result_list

    def avgPrice (self):
        self.book_list = self.getAll()
        sumPrice = 0
        for book in self.book_list:
            sumPrice += book['price']

        avg = sumPrice/len(self.book_list)
        return [f'Avarege Price:{avg}']


#class Bookstore(Start Page [optional] as Integer, Last Page [optional] as Integer)
#store = Bookstore(45)
#store = Bookstore(45, 47)
store = Bookstore()

#getAll() Get all the book data as a list
#result_list = store.getAll()


#priceFilter(minimum price as Integer, maximum price as Integer)
#result_list = store.priceFilter(20, 50)

#starFilter(minimum star as Integer, maximum star [optional] as Integer)
#result_list = store.starFilter(3, 5)
#result_list = store.starFilter(3)

#searchName(Search Text as String [Minimum 3 charachter])
#result_list = store.searchName('Places')

#Avarage prices in Bookstore
result_list = store.avgPrice()


for book in result_list:
    print(book)

print(f"{str(len(result_list))} result returned.")
