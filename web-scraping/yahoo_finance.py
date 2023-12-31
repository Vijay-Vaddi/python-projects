import requests
from bs4 import BeautifulSoup

company_list = ['AMZN', 'TSLA', 'GME', 'AMD', 'AAPL', 'GOOG']

def getStockData(orgs):
    stock_data = []
    for org in orgs:
        url = f"https://finance.yahoo.com/quote/{org}"
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        stock = {
            'price' : soup.find('fin-streamer', {'class':"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text,
            'change' : soup.find('fin-streamer', {'class':"Fw(500) Pstart(8px) Fz(24px)"}).text
        }
        stock_data.append(stock)
        
    return stock_data

print(getStockData(company_list))