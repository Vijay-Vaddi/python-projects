import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select("[rel='noreferrer']")  
votes = soup.select('.score') 

#create a function to clear and append needed data into a dic

def create_custom_hn(votes, links):
    hn = []
    for i, link in enumerate(links):
        link_of_title = links[i].get('href', None) #if nothing exists
        points = int(votes[i].getText().replace(' points', ''))
        title = links[i].getText()
        
        if points>99:
            hn.append({'link':link_of_title,
                       'title':title,
                       'points':points})
    return sorted(hn, key=lambda hn: hn['points'], reverse=True)

pprint.pprint(create_custom_hn(votes, links))