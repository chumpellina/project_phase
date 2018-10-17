from bs4 import BeautifulSoup
import pandas as pd
import lxml

infile = open("index.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents, "lxml-xml")
titles = soup.find_all('title')
titles_list =[]
for title in titles:
    if title.text.startswith("\n") == True:
        title.string = title.text[2:]
        titles_list.append(title)

df = pd.DataFrame (titles_list)
print (df)



