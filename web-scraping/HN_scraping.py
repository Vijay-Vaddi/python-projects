import requests
from bs4 import BeautifulSoup

# requests allows us to download html
# BS allows to use HTML and grab diff data/scraping

# requests is web browser without window. underneat browsers. they sent requests
res = requests.get('https://news.ycombinator.com/')
#res comes in document (html inside) from the network
# so we do res.text
# print(res.text)

#BS allows to parse, convert from string to an object we can manipulate
# modify into html that we can parse, becomes soup object
# BS also parser xml and others
# what does HTML.parser do?

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body) #grabs just body, can do head, etc
# print(soup.body.contents) #contents??

# print(soup.find('div')) #returns first one
# print(soup.find_all('span', class_="score")) #searches and returns all elements
# print(soup.find('.score')) #works on soup.select

# print(soup.select('.score')) #used for CSS class selectors

# link = soup.find('link', {'rel':'nonreferrer'})['href'] 
# #passing dictionary. check again
#get links and votes 
links = soup.select("[rel='noreferrer']")  
votes = soup.select('.score') #votes = soup.select('.score').select() to get more info

# print(votes[0].getText().replace(' points', ''))
print(links[0].get_text())
print(int(votes[0].getText().replace(' points', '')))
   
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

print(create_custom_hn(votes, links))