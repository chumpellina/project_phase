import requests
import bs4 as bs
import pandas as pd
import lxml

main_page = requests.get("http://hvg.hu")
content = bs.BeautifulSoup(main_page.text, "lxml")

titles = content.find_all("p")
titles_list = []

for title in titles:
    for child in title.children:
        if child.name is None and child !="\n":
            titles_list.append(child)


df = pd.DataFrame (titles_list, index= "index" ,columns= "Title")

print(df)
