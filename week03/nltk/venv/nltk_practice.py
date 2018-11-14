
import nltk, re, pprint
import urllib
from urllib.request import urlopen
import pandas as pd
import xlrd
from nltk.probability import FreqDist
import operator
from nltk.tokenize import word_tokenize


filename = "my_final_data.xlsx"
df = pd.read_excel(filename)

#melyik oszlop szövegeit akarjuk elemezni
my_Series = pd.Series(df["text"])
my_text = my_Series.str.cat (sep=' ')


#tokenizálás
word_tokens = word_tokenize(my_text)


#remove stop words
stop_words= {'már', 'Már', 'alá', 'Alá', 'a', 'A', 'az', 'Az', 'azt', 'Azt', 'egy', 'Egy', 'ha', 'Ha', 'hogy', 'Hogy', 'akkor', 'Akkor', 'kell', 'Kell',
	'nem', 'Nem', 'igen', 'Igen', 'én', 'Én', 'te', 'Te', 'ő', 'Ő', 'mi', 'Mi', 'ti', 'Ti', 'ők', 'Ők', 'ahogy', 'Ahogy' 'és', 'És', 'is', 'Is', 'lehet',
	'Lehet', 'amit', 'Amit', 'de', 'De', 'most', 'Most', 'ad', 'Ad', 'aki', 'Aki', 'mint', 'Mint', 'alatt', 'Alatt', 'ami', 'Ami',
	'szerző', 'Szerző', 'így', 'Így', 'sem', 'Sem', 'van', 'Van', 'nincs', 'Nincs', 'helyett', 'Helyett', 'ezt', 'Ezt', 'ez', 'Ez', 'meg', 'Meg', 'után',
	'Után', 'vagy', 'Vagy', 'így', 'Így', 'úgy', 'Úgy', 'amúgy', 'Amúgy', 'fel', 'Fel', 'le', 'Le', 'arra', 'Arra', 'erre', 'Erre', 'főleg', 'Főleg', 'persze',
	'Persze', 'és', 'És', 'lenne', 'Lenne', 'minden', 'Minden', 'lesz', 'Lesz', '', 'el', 'El', 'meg', 'Meg', 'fel', 'Fel', 'ne', 'Ne', 'még', 'Még', 'csak', 'CSak'}

filtered_tokens = [w for w in word_tokens if not w in stop_words]


#maradék tokenekből egy stringet csinálni
tokens_string = ", ".join(filtered_tokens)


# a maradék tokenek frekvenciáit kiszedni
blabla = re.split(r"\W",tokens_string.lower())
freq = {}
for word in blabla:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1


# frekvencia alapján sorba állít   --  a fenti dictionaryból csinál egy listát, amiben tuple-k vannak (első elem szó, második a gyakorisága)
sorted_freq = sorted(freq.items(), key=operator.itemgetter(1))


# eltávolítja azon tokeneket, amelyek csak egyszer fordulnak elő - NEM MŰKÖDIK
for item in sorted_freq:
    if item[1]==1:
        sorted_freq.remove(item)


#Leggyakoribb 10 elem kiiratása
print (sorted_freq[-50:])













