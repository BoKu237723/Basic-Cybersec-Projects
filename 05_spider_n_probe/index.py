# https://en.wikipedia.org/wiki/Vibe_coding
# https://boards.4chan.org/ck/

import requests
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')

    # print(soup.a) # grab the first <a></a> tag
    # print(soup.find("a")) # also grab the first <a></a> tag
    # print(soup.find_all("a")) # find all <a></a> tags
    # print(soup.find(id = "t22058676")) # find specific id
    # print(soup.title.string) # print out the title of the web-page
    
    tag = soup.find_all("a")
    for t in tag:
        url2 = t.get("href")
        print(url2)
    # print(tag)

get_page(input("Enter URL to scrape: "))





























