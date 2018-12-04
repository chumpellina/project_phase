from pymongo import MongoClient
import numpy as np
import pandas as pd

client = MongoClient(
    'ec2-35-158-191-40.eu-central-1.compute.amazonaws.com', 27017)


def dump_into_df(db_name):
    db = client[db_name]
    collection = db.scrapy_items
    return pd.DataFrame(list(collection.find({})))


pd.set_option('display.width', 10000)
pd.set_option('display.max_rows', 20000)
pd.set_option('display.max_columns', 10000)
#pd.set_option('display.max_colwidth', -1)

df = dump_into_df("beer")

if ['brewery'] == "rizmajersor.hu":
    df["new_alcohol_vol"] = df["ingredients"]
else:
    df["new_alcohol_vol"] = df["alcohol_vol"]

#df["new_alcohol_vol"].replace(None, "NaN")
#df.replace(r"[A-Za-z]", " ")

#df.to_excel("mydadadadadadta.xlsx")
print (df)






