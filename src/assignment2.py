import requests #we need to import requests and BeautifulSoup 
from bs4 import BeautifulSoup

class scaper:#Class that scraps posts about specific cryptocurrencies 
    #please use lowercase letters
    name = input('Insert a cryptocurrency:')
    #take information from coinmarketcap.com a news page about given crypto
    host = "https://coinmarketcap.com/ru/currencies/"+name+"/news/"
    #taking a requests
    site = requests.get(host)
    #using a beatifulsoup
    bSoup = BeautifulSoup(site.text, 'html.parser')
    #it finds first html code with 'meta' attribute and with specific property
    siteName = bSoup.find("meta", property="og:image")

    title = siteName['content']

    id =  title.rpartition('/')[2].rpartition('.')[0]

    result = requests.get('https://api.coinmarketcap.com/content/v3/news?coins='+id+'&page=1&size=20')

    data = result.json()#refactoring to .json format
    def printScraping(self):#method that will print all results
        for i in range(20):
            #first 20 posts only, it can be bigger, but you need to change range and in line 20 change '&page=1&size='number, it should be equal as a number in range in range'
            print('Site:\n')
            print(self.data.get('data')[i].get('meta').get('subtitle'))
            url = self.data.get('data')[i].get('meta').get('sourceUrl')
            pages = requests.get(url)
            bSoup2 = BeautifulSoup(pages.text, 'html.parser')
            paragraphs = bSoup2.findAll('p', limit=None)#finds all paragraphs
            for i in range(len(paragraphs)):
                print(paragraphs[i].text)
            print('\n Link is ')#will print link after posting all information
            print(url+'\n')#url


