import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns
sns.set(style="whitegrid")
import math
from sklearn import linear_model
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


pd.set_option('display.width', 10000)
pd.set_option('display.max_rows', 20000)
pd.set_option('display.max_columns', 10000)
#pandas.set_option('display.max_colwidth', -1)

### Dataset
filename = "tiszta_sor_adatok.xlsx"
df = pd.read_excel(filename)
# print(df)
print(df.isnull().sum())
df2 = df.drop(labels=["_id", "balling", "beer_name", "beer_type", "brewery", "description", "dry_matter", "ebc", "ingredients", "price", "temperature", "vol", "is_duplicate", "alcohol_plus", "bitterness_plus", "fruity_check", "fruity"], axis=1)
msno.matrix(df2)
plt.show()


### Correlation & Boxplot
df2 = df[df.alcohol_vol.notnull() & df.bitterness.notnull() & df.color.notnull()]
df2 = df2[df2.brewery.notnull()]

# Boxplot ide

print(df2.alcohol_vol.describe())
df2 = df2[df2.alcohol_vol != 45]
df2 = df2[df2.alcohol_vol != 40]
# Esetleg kizarni color es bitterness alapjan is
print(df2.shape)   # 99 sor
print(df2.head())

## Correlations - coeffs
print(np.corrcoef(df2.bitterness, df2.color))
print(np.corrcoef(df2.alcohol_vol, df2.color))
print(np.corrcoef(df2.bitterness, df2.alcohol_vol))

## Correlations - plots
pairplot_df2 = df2.loc[:, ['alcohol_vol', 'color']]
sns.set(style="dark")
sns.pairplot(data=pairplot_df2)
plt.show()

pairplot_df2 = df2.loc[:, ['alcohol_vol', 'bitterness']]
sns.set(style="dark")
sns.pairplot(data=pairplot_df2)
plt.show()

pairplot_df2 = df2.loc[:, ['color', 'bitterness']]
sns.set(style="dark")
sns.pairplot(data=pairplot_df2)
plt.show()

## !!!Weak correlation, no linear relationship, quite high variance!!!

### Missing data imputation: linear regression: if we have 2 info from 3 + Mean/Mode

## Linear regression
# Source: https://datatofish.com/multiple-linear-regression-python/
# We assume the color, the bitterness and the alcohol content are strongly correlated each other!


## Reg1 - 6 imputalas
X = df2[['bitterness', 'color']]
Y = df2['alcohol_vol']

regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
print(regr.score(X, Y))   # Source: https://www.ritchieng.com/machine-learning-evaluate-linear-regression-model/

df['imp_alc'] = 5.27173673172242 + 0.02073145 * df['bitterness'] + 0.01353464 * df['color']
# print(df[['imp_alc', 'alcohol_vol']])
# print(df['imp_alc'].shape)

df['alcohol_vol_orig'] = df['alcohol_vol']
df.loc[df['alcohol_vol'].isnull(), ['alcohol_vol']] = df['imp_alc']
# print(df[['alcohol_vol_orig', 'imp_alc', 'alcohol_vol']])


## Reg2 - 23 imputalas
X = df2[['bitterness', 'alcohol_vol']]
Y = df2['color']

regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
print(regr.score(X, Y))

df['imp_color'] = -19.845720549312134 + 0.05539463 * df['bitterness'] + 9.31376037 * df['alcohol_vol']
print(df)
print(df['imp_color'].shape)

df['color_orig'] = df['color']
df.loc[df['color'].isnull(), ['color']] = df['imp_color']
print(df[['color_orig', 'imp_color', 'color']])


## Reg3 - 4 imputalas
X = df2[['color', 'alcohol_vol']]
Y = df2['bitterness']

regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
print(regr.score(X, Y))

df['imp_bitt'] = 13.590383939982672 + 0.01180317 * df['color'] + 3.03975753 * df['alcohol_vol']
print(df)
print(df['imp_bitt'].shape)

df['bitterness_orig'] = df['bitterness']
df.loc[df['bitterness'].isnull(), ['bitterness']] = df['imp_bitt']
print(df[['bitterness_orig', 'imp_bitt', 'bitterness']])
print(df.isnull().sum())
df2 = df.drop(labels=["_id", "balling", "beer_name", "beer_type", "brewery", "description", "dry_matter", "ebc", "ingredients", "price", "temperature", "vol", "is_duplicate", "alcohol_plus", "bitterness_plus", "fruity_check", "fruity"], axis=1)
msno.matrix(df2)
plt.show()
## Print mean/mode/median
print(df.alcohol_vol.describe().apply(lambda x: format(x, 'f')))
print(df.alcohol_vol.mode())
df.loc[df['alcohol_vol'].isnull(), ['alcohol_vol']] = df.alcohol_vol.mean()

print(df.bitterness.describe().apply(lambda x: format(x, 'f')))
print(df.bitterness.mode())
df.loc[df['bitterness'].isnull(), ['bitterness']] = df.bitterness.mean()

print(df.color.describe().apply(lambda x: format(x, 'f')))
print(df.color.mode())
df.loc[df['color'].isnull(), ['color']] = df.color.mean()
print(df.isnull().sum())


### PLOTTING
## Missing value visualisation - need more work!
df2 = df.drop(labels=["_id", "balling", "beer_name", "beer_type", "brewery", "description", "dry_matter", "ebc", "ingredients", "price", "temperature", "vol", "is_duplicate", "alcohol_plus", "bitterness_plus", "fruity_check", "fruity", "imp_alc", "alcohol_vol_orig", "imp_color", "color_orig", "imp_bitt", "bitterness_orig"], axis=1)
msno.matrix(df2)
plt.show()

## Boxplot - outlier with red
# https://stackoverflow.com/questions/35131798/tweaking-seaborn-boxplot
myvar = ['alcohol_vol']
f, ax = plt.subplots(figsize=(8, 6))
flierprops = dict(markerfacecolor="red", markersize=5,
              linestyle='none')
ax = sns.boxplot(data=df2.loc[:, myvar], orient='h', flierprops=flierprops)
ax.set(title='Boxplot', xlabel='Alcohol content')
plt.show()

myvar = ['bitterness']
f, ax = plt.subplots(figsize=(8, 6))
flierprops = dict(markerfacecolor="red", markersize=5,
              linestyle='none')
ax = sns.boxplot(data=df2.loc[:, myvar], orient='h', flierprops=flierprops)
ax.set(title='Boxplot', xlabel='Bitterness')
plt.show()

myvar = ['color']
f, ax = plt.subplots(figsize=(8, 6))
flierprops = dict(markerfacecolor="red", markersize=5,
              linestyle='none')
ax = sns.boxplot(data=df2.loc[:, myvar], orient='h', flierprops=flierprops)
ax.set(title='Boxplot', xlabel='Color')
plt.show()

df['imp_color'] = -19.845720549312134 + 0.05539463 * df['bitterness'] + 9.31376037 * df['alcohol_vol']