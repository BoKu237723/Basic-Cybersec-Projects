# https://boards.4chan.org/ck/


import requests
from bs4 import BeautifulSoup
from urllib import *
from urllib.parse import urljoin

visited_urls = set()

def spider_urls(url, keywords):
    try:
        response = requests.get(url)
        print(response.status_code)
    except Exception as e:
        print(f"Request failed: {e}")
        return
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        # print(urls)

        try:
            for i in urls:
                if i not in visited_urls:
                    visited_urls.add(i)
                    url_join = urljoin(url, i)
                    if keyword in url_join:
                        print(url_join)
                        spider_urls(url_join, keyword)
                else:
                    pass
        except KeyboardInterrupt:
            with open("scraped_urls.txt", "a", encoding = "utf-8") as f:
                for unique_url in visited_urls:
                    f.write(f"{urljoin(url, unique_url)}\n")

            print("Program paused by Keyboard Interruption.")
            quit()

url = input("Enter the URL to scrape: ")
keyword = input("Enter the keyword to search for: ")
spider_urls(url, keyword)





