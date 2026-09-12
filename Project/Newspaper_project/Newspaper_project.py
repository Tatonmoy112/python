import requests
import json
qurey=input("what type of news are you interested in? ")
url=f"https://newsapi.org/v2/everything?q={qurey}&from=2024-06-05&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7"

r=requests.get(url)
news=json.loads(r.text)
print("-----------")
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------------")