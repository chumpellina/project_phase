from __future__ import division
import nltk, re, pprint
import urllib
from urllib.request import urlopen
import feedparser
llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
post = llog.entries[2]
print (post.title)

a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
b = [' ' * 2 * (7 - i) + 'very' * i for i in a]
for line in b:
    print (line)