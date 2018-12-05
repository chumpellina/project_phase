import pandas as pd
import numpy as np
from sklearn import linear_model

pd.set_option('display.width', 10000)
pd.set_option('display.max_rows', 20000)
pd.set_option('display.max_columns', 10000)
#pandas.set_option('display.max_colwidth', -1)

df = pd.read_excel("tiszta_sor_adatok.xlsx")
df2 = df.drop(labels=["_id", "balling", "beer_name", "beer_type", "brewery", "description", "dry_matter", "ebc", "ingredients", "price", "temperature", "vol", "is_duplicate", "alcohol_plus", "bitterness_plus", "fruity_check", "fruity"], axis=1)
df3 = df2.dropna(axis = 0)
df4 = df2[df2.alcohol_vol.isnull() & df2.color.notnull() & df2.bitterness.notnull()]
df6 = df2[df2.alcohol_vol.notnull() & df2.color.notnull() & df2.bitterness.isnull()]
df8 = df2[df2.alcohol_vol.notnull() & df2.color.isnull() & df2.bitterness.notnull()]
print (df3.describe())

#MISSING ALCOHOL_VOL
reg = linear_model.LinearRegression ()
reg.fit(df3[["color", "bitterness"]], df3.alcohol_vol)
df5 = df4.drop(labels="alcohol_vol", axis = 1)
#print(df5)
#print (reg.predict(df5))
#print (reg.coef_)
#print (reg.intercept_)

#MISSING BITTERNESS
regtwo = linear_model.LinearRegression ()
regtwo.fit(df3[["color", "alcohol_vol"]], df3.bitterness)
df7 = df6.drop(labels="bitterness", axis = 1)
#print (df7)
#print (reg.predict(df7))
#print (regtwo.coef_)
#print (regtwo.intercept_)

#MISSING COLOR
regthree = linear_model.LinearRegression ()
regthree.fit(df3[["alcohol_vol", "bitterness"]], df3.color)
df9 = df8.drop(labels="color", axis = 1)

print (df9)
print (reg.predict(df9))
print (regthree.coef_)
print (regthree.intercept_)

