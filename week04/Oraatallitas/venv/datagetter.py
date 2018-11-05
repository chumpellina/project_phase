from bs4 import BeautifulSoup
import requests
import lxml
import feedparser


source = requests.get("https://888.hu/search-%C3%B3ra%C3%A1t%C3%A1ll%C3%ADt%C3%A1s").text

forras = []
cim = []
lead = []
datum = []
szoveg = []
tagek = []

soup = BeautifulSoup(source, "lxml")

for cimek in soup.find_all("div", class_="main-content"):
    cim.append (cimek.h2)
    forras.append (cimek.a)
    print(cimek.prettify())



