import requests
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def opening_page (target):
    splitted_target = target.split(" ")
    url = "https://en.wikipedia.org/wiki/" + splitted_target[0] + "_" + splitted_target[1]
    client = uReq(url)
    page_html = client.read()
    page_soup = soup (page_html, "html.parser")
    tags = page_soup.findAll("a", {"title":"Chess Records"})
    references = []
    for tag in tags:
        references.append("https://en.wikipedia.org" + tag["href"])
    return references