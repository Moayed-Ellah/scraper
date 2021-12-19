import requests
from bs4 import BeautifulSoup
from collections import Counter

URL = "https://moayedellah.tk"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
job_elements = soup.find("html")
output = print(job_elements.text)
split_it = output.split()
  

Counter = Counter(split_it)
most_occur = Counter.most_common(4)
  
print(most_occur)