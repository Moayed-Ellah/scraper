# imports

import requests
from bs4 import BeautifulSoup

# defining input

link = input("input the website link here: ")
page = requests.get(link)


# soup scraping the content in all h1 divs
soup = BeautifulSoup(page.content, "html.parser")
element = soup.find("h1")
output = print(element.text)
