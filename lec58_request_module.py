import requests
from bs4 import BeautifulSoup
response=requests.get("https://codewithharry.com")
# print(response.text)

soup=BeautifulSoup(response.text,"html.parser")
print(soup.prettify())