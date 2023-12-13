import requests
from bs4 import BeautifulSoup

# requests allows us to download html
# BS allows to use HTML and grab diff data/scraping

# requests is web browser without window. underneat browsers. they sent requests
res = requests.get('https://news.ycombinator.com/')
#res comes in document (html inside) from the network
# so we do res.text
print(res.text)

