import requests
from bs4 import BeautifulSoup
import pprint

def multi_page_data(pages_length):
    page_num = 0
    complete_data = []
    while page_num<=pages_length:
        res = requests.get(f'https://news.ycombinator.com/news?p={page_num}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select("[rel='noreferrer']")  
        votes = soup.select('.score') 
        page = create_custom_hn(votes,links)
        complete_data = complete_data+page
        page_num+=1
    
    return sorted(complete_data, key=lambda complete_data: complete_data['points'], reverse=True) 


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
    return hn

pprint.pprint(multi_page_data(2))