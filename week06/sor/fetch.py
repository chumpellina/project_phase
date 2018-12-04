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
#pandas.set_option('display.max_colwidth', -1)

df = dump_into_df("newbeer")


#kiszedjük a brewery szerinti nullokat
df = df[df.brewery.notnull()]


# Check duplicates - no duplicates
df["is_duplicate"] = df.duplicated()


# DECIDING THE TYPE OF THE BEER:
df["beer_type_new"] = ''
beer_types = ['IPA', 'APA', 'Pale Ale', 'Blonde Ale', 'Amber Ale', 'Brown Ale', 'Stout', 'Porter', 'Lager', 'Wheat', 'Pilsner', 'Saison']
ipa_names = ['ipa', 'indian pale ale']
apa_names = ['apa', 'american pale ale']
wheat_names = ['buza', 'búza', 'weizen', 'wheat', 'weisse', 'witbier']
pils_names = ['pils', 'pilz']

# getting the beer types from their description
df = df[df.description != 158]

for index, descrip in enumerate(df["description"]):
    if type(descrip) is str :
        for btype in beer_types:
            if btype.lower() in descrip.lower():
                df.loc[df.index[index], "beer_type_new"] = btype
        for itype in ipa_names:
            if itype in descrip.lower():
                df.loc[df.index[index], "beer_type_new"] = 'IPA'
        for atype in apa_names:
            if atype in descrip.lower():
                df.loc[df.index[index], "beer_type_new"] = 'APA'
        for wtype in wheat_names:
            if wtype in descrip.lower():
                df.loc[df.index[index], "beer_type_new"] = 'Wheat'
        for ptype in pils_names:
            if ptype in descrip.lower():
                df.loc[df.index[index], "beer_type_new"] = 'Pilsner'

# getting the beer types from their names
for index, name in enumerate(df["beer_name"]):
    if 'ale' in name.lower():
        df.loc[df.index[index], "beer_type_new"] = 'Ale'
    for btype in beer_types:
        if btype.lower() in name.lower():
            df.loc[df.index[index], "beer_type_new"] = btype
    for itype in ipa_names:
        if itype in name.lower():
            df.loc[df.index[index], "beer_type_new"] = 'IPA'
    for atype in apa_names:
        if atype in name.lower():
            df.loc[df.index[index], "beer_type_new"] = 'APA'
    for wtype in wheat_names:
        if wtype in name.lower():
            df.loc[df.index[index], "beer_type_new"] = 'Wheat'
    for ptype in pils_names:
        if ptype in name.lower():
            df.loc[df.index[index], "beer_type_new"] = 'Pilsner'
df.replace({"beer_type_new": [None, " ", "  ", "  "]}, "NaN")



## Clean alc_vol
df.alcohol_vol = (df.alcohol_vol.str.strip().str.replace('\n', '').str.replace('%', '').str.replace('°', '').
                      str.replace(',', '.').str.replace('ALKOHOL: ', '').str.replace('(V/V)', '').str.replace('(', '').str.replace(')', ''))

df.loc[134:136, ['alcohol_vol']] = "NaN"
df.loc[138:140, ['alcohol_vol']] = "NaN"
df.loc[142:148, ['alcohol_vol']] = "NaN"
df.loc[158, ['alcohol_vol']] = "NaN"
df.loc[201, ['alcohol_vol']] = "NaN"
df.loc[203:208, ['alcohol_vol']] = "NaN"
df.loc[210:211, ['alcohol_vol']] = "NaN"
df.loc[214, ['alcohol_vol']] = "NaN"
df.loc[216, ['alcohol_vol']] = "NaN"
df.loc[220, ['alcohol_vol']] = "NaN"
df.loc[225:229, ['alcohol_vol']] = "NaN"

## Find more alc
df['alcohol_plus'] = df["description"].str.extract(r'\s(\d+\,?\d*)\s?\%', expand=False).fillna('Original')

df.loc[df['alcohol_vol'].isnull(), ['alcohol_vol']] = df['alcohol_plus']

df["alcohol_vol"] = df["alcohol_vol"].str.replace('Original', 'NaN').str.replace(',', '.')

df["alcohol_vol"] = df.alcohol_vol.astype(float)

## 5 alatt 0, azaz gyenge, 5-7 közt közepes, tehát 1, és 7 fölött erős, azaz 2
# df['alc'] = 9
# df.loc[df['alcohol_vol'] < 5.0, ['alc']] = 0
# df.loc[df['alcohol_vol'].between(5.0, 6.9), ['alc']] = 1
# df.loc[df['alcohol_vol'] >= 7.0, ['alc']] = 2


#BITTERNESS

## Clean bitterness
df.bitterness = (df.bitterness.str.strip().
                 str.replace(' IBU', '').
                 str.replace('IBU: ', '').
                 str.replace(',', '.'))

df.loc[133:136, ['bitterness']] = "NaN"
df.loc[138, ['bitterness']] = "NaN"
df.loc[140:141, ['bitterness']] = "NaN"
df.loc[143, ['bitterness']] = "NaN"
df.loc[145:146, ['bitterness']] = "NaN"
df.loc[201:202, ['bitterness']] = "NaN"
df.loc[204:208, ['bitterness']] = "NaN"
df.loc[210:211, ['bitterness']] = "NaN"
df.loc[214, ['bitterness']] = "NaN"
df.loc[216, ['bitterness']] = "NaN"
df.loc[219:220, ['bitterness']] = "NaN"
df.loc[222, ['bitterness']] = "NaN"
df.loc[225:229, ['bitterness']] = "NaN"

## Find more bitterness
df['bitterness_plus'] = df['bitterness']
df.loc[df['bitterness'] == "NaN", ['bitterness']] = df["description"].str.extract(r'\s(\d+\,?\.?\d*?)\s?IBU', expand=False)

df["bitterness"] = df["bitterness"].str.replace(',', '.')
df.loc[149, ['bitterness']] = "70"
df["bitterness"] = df["bitterness"].astype(float)


#FRUITiNESS

## Fruity
df['fruity_check'] = df['description'].str.extract(r'(Banán|Gyömbér|Mango|Passion Fruit|Blackberry|gyümölcsös|déligyümölcsös|'
                                                   r'Gyümölcsös|citrusos|szőlő|vörösáfonyával|Málnás|lime|citrom|Raspberry|'
                                                   r'Uborkás|Gyümölcs|gyümölcs|málna|mango|banán|mandarin|ananász|narancs|'
                                                   r'meggy|grapefruit|Apricot|Banana|Watermelon|bodza|cigánymeggyel)')
df['fruity'] = 0
df.loc[df['fruity_check'].notnull(), ['fruity']] = 1





# COLOR

df["color"] = df["color"].str.replace("Színe: ", "")\
    .str.strip()\
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

df.loc[134:136, ['color']] = "NaN"
df.loc[138, ['color']] = "NaN"
df.loc[140:141, ['color']] = "NaN"
df.loc[143:146, ['color']] = "NaN"
df.loc[201, ['color']] = "NaN"
df.loc[204:208, ['color']] = "NaN"
df.loc[210:211, ['color']] = "NaN"
df.loc[214, ['color']] = "NaN"
df.loc[216:217, ['color']] = "NaN"
df.loc[219:220, ['color']] = "NaN"
df.loc[225:229, ['color']] = "NaN"
df.loc[8, ['color']] = "5"

pd.to_numeric(df["color"], errors='coerce', downcast="float")
df.color =df["color"].astype(float)
df["color"].convert_objects(convert_numeric=True)

df.loc[df['brewery'] == 'Monyo Budapest', ['color']] = df["color"]*2


#print(df["color"].describe(), df["fruity"].describe(), df["bitterness"].describe(), df["alcohol_vol"].describe(), df["beer_type_new"].describe())
print (df["color"])


