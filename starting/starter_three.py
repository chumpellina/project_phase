import numpy as np
import pandas as pd

filename = "googleplaystore.csv"
df = pd.read_csv(filename)
pd.set_option('display.width', 10000)
pd.set_option('display.max_rows',15)
pd.set_option('display.max_columns',500)

#Sort-tal kiderítem, hogy melyik a legalsó Review pontszám, majd kifilterezem azokat az appokat, amelyeknek ennyi a pontszáma
df.sort_values("Reviews")
print (df[df.Reviews == "0"])
#Rating deskriptív adatai (közte átlag) + medián + modus
print (df.Rating.describe(), df.Rating.median, df.Rating.mode())
print (df.Size.describe(), df.Size.median, df.Size.mode())

