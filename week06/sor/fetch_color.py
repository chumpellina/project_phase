#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

import pandas as pd
import numpy as np


client = MongoClient(
    'ec2-35-158-191-40.eu-central-1.compute.amazonaws.com', 27017)


def dump_into_df(db_name):
    db = client[db_name]
    collection = db.scrapy_items
    return pd.DataFrame(list(collection.find({})))

pd.set_option('display.width', 10000)
pd.set_option('display.max_rows', 20000)
pd.set_option('display.max_columns', 10000)
pd.set_option('display.max_colwidth', -1)

df = dump_into_df("newbeer")

df["color"] = df["color"].str.replace("Színe: ", "")\
    .str.replace("borostyán", "27")\
    .str.replace("szalmasárga", "3")\
    .str.replace("világos ", "")\
    .str.replace("sötét ", "")\
    .str.replace("barna", "60")\
    .str.replace("vörös", "48")\
    .str.replace("sárga", "6")\
    .str.replace (" EBC", "")\
    .str.replace(";", "")\
    .str.replace(",", ".")

df["color"].convert_objects(convert_numeric=True)

df.loc[df['brewery'] == 'Monyo Budapest', ['color']] = df["color"]*2

print (df["color"].describe())





