import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AMZN"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
#without adding user agent yf was giving false/static data.

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

# print(soup.title.text) #to test if its working. a good method and a step. 
# print(soup)

price = soup.find('fin-streamer', {'class':"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
change = soup.find('fin-streamer', {'class':"Fw(500) Pstart(8px) Fz(24px)"}).text
print(price, change)

