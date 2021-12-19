import requests
from bs4 import BeautifulSoup


link = input("input the website link here: ")

page = requests.get(link)



soup = BeautifulSoup(page.content, "html.parser")
element = soup.find("h1")
output = print(element.text)
