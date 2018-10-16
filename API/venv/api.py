from bs4 import BeautifulSoup
import pandas as pd
import lxml

infile = open("index.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents, "lxml-xml")
titles = soup.find_all('title')
titles_list =[]
for title in titles:
    #if title.get_text.startswith("\n") == True:
        #title = title[2:]
        titles_list.append(title.get_text())

df = pd.DataFrame (titles_list)
print (df.iloc[6])



