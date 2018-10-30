from bs4 import BeautifulSoup
import requests


source = requests.get("http://index.hu").text
soup = BeautifulSoup(source, "lxml")
titles = []
links =[]
texts=[]
for article in soup.find_all("h1", class_="cikkcim"):
    titles.append (article.text)
    links.append(article.a["href"])

'''for link in links:
    newsource = requests.get(link).text
    mytext = BeautifulSoup(newsource, "lxml")
    textcore = mytext.find("div", class_ = "cikk-torzs")
    if textcore != None:
        texts.append(textcore.text)'''

print (titles)


