import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot
import matplotlib.pyplot as plt
import sklearn

pd.set_option('display.width', 10000)
pd.set_option('display.max_rows', 20000)
pd.set_option('display.max_columns', 10000)

df = pd.read_excel("mysuperdata.xlsx",  sep='delimiter', header=None)
df_two = pd.read_excel("newtable.xlsx",  sep='delimiter')

#df_two['new_alcohol_vol'] = df_two['new_alcohol_vol'].str.replace(',', '.')
df_two['new_alcohol_vol'] = pd.to_numeric(df_two['new_alcohol_vol'])
#hist = matplotlib.pyplot(df_two['new_alcohol_vol'])

num_bins = 117
n, bins, patches = plt.hist(df_two['new_alcohol_vol'], num_bins, facecolor='blue', alpha=0.5)
plt.ylabel('Count')
plt.xlabel('Alcohol content')
plt.show()


text = str(response.xpath('//*[@id="tab-description"]/div/div/p[2]/text()')
           .extract())
pattern_alc = re.compile(r"(\d{1,2}[\.\,]d{1,2}|\d{1,2})\s?\%?")
item['alcohol_vol'] = pattern_alc.findall(text)
