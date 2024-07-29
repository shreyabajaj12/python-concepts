import requests
import json
query=input("what type of news are you intrested in? ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-11-03&sortBy=publishedAt&apiKey=b4c64c0ec7114410ba2f2c6e2859fa69"
r=requests.get(url)
news=json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------------------")
