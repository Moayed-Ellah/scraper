<h1 align="center">Scraper</h1>
<hr>

> scraper is a python simple web scraper, you can give an input and wait for the code to fetch the data from the listed website, you can change the websites you want to scrap on an input

<hr>

# the imports needed, soup & requests

```diff
! import requests
! from bs4 import BeautifulSoup
```

# defining the input variable, take input from end-user and use it as the link input

```diff
link = input("input the website link here: ")
```

# using request to fetch the link of the website given

```diff
page = requests.get(link)
```

# the rest is left for soup to handle, you can change the "h1" to the class element you're after, or replace it with the div id instead

```diff
soup = BeautifulSoup(page.content, "html.parser")
element = soup.find("h1")
output = print(element.text)
```
