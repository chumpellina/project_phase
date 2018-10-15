import numpy as np
import pandas as pd

filename = "googleplaystore.csv"
df = pd.read_csv(filename, na_values = "Varies with device")
pd.set_option('display.width', 10000)
pd.set_option('display.max_rows',20000)
pd.set_option('display.max_columns',10000)

#kiszedni a duplikátumokat
df.drop_duplicates(keep='first', inplace=True)

#kiszedni az elcsúszott sort
df[df["Installs"] != 'Free']

#kiszedni az egyes oszlopok invalid elemeit
df[(df["Rating"]>=0) & (df["Rating"]<=5)]
df[(df['Type'] != 'Free') & (df['Type'] != 'Paid')]

#átváltani a Mb, Kb-okat



print (df)
#print (df[df.Reviews == "0"])
#Rating deskriptív adatai (közte átlag) + medián + modus
#print (df.Rating.describe(), df.Rating.median, df.Rating.mode())
#print (df.Size.describe(), df.Size.median, df.Size.mode())

