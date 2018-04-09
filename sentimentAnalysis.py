
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:07:21 2016

@author: Tanvi
"""
from textblob import TextBlob
import json
import os
import numpy as np
from wordcloud import WordCloud
import nltk
import matplotlib.pyplot as plt
#from nltk.stem.porter import PorterStemmer


#import nltk
#stopwords = nltk.corpus.stopwords.words('english')
jsonObamaFiles,jsonTrumpFiles,jsonClintonFiles = [],[],[]
obama = ''
trump = ''
clinton = ''
polObama,subObama = [],[]
polTrump,subTrump = [],[]
polClinton,subClinton=[],[]

for files in os.listdir('./json'):
    if files.endswith('json') and 'Obama' in files:
        jsonObamaFiles.append(files)
    elif files.endswith('json') and 'Trump' in files:
        jsonTrumpFiles.append(files)
    elif files.endswith('json') and 'Clinton' in files:
        jsonClintonFiles.append(files)
#os.chdir('./json')
for filename in jsonObamaFiles:
    infile = open(filename).read()
    content = json.loads(infile)
    for i in range(200):        
        tweet = content[i]['text']
        obama += tweet + '\n'
        senObama = TextBlob(tweet)
        polObama.append(senObama.sentiment.polarity)
        subObama.append(senObama.sentiment.subjectivity)
for filename in jsonTrumpFiles:
    infile = open(filename).read()
    content = json.loads(infile)
    for i in range(200):        
        tweet = content[i]['text']
        trump += tweet + '\n' 
        senTrump = TextBlob(tweet)
        polTrump.append(senTrump.sentiment.polarity)
        subTrump.append(senTrump.sentiment.subjectivity)
for filename in jsonClintonFiles:
    infile = open(filename).read()
    content = json.loads(infile)
    for i in range(200):        
        tweet = content[i]['text']
        clinton += tweet + '\n' 
        senClinton = TextBlob(tweet)
        polClinton.append(senClinton.sentiment.polarity)
        subClinton.append(senClinton.sentiment.subjectivity)

print('{} {} {}'.format(np.mean(polObama),np.mean(polTrump),np.mean(polClinton)))
print('{} {} {}'.format(np.mean(subObama),np.mean(subTrump),np.mean(subClinton)))
print('{} {} {}'.format(len(subObama),len(subTrump),len(subClinton)))
################################################################################################

stopwords = nltk.corpus.stopwords.words('english')
stopwords.append(u'https')
stopwords.append(u'http')
stopwords.append(u'rt')

wcObama = WordCloud(max_font_size=40,stopwords=stopwords).generate(obama.lower())
wcTrump = WordCloud(max_font_size=40,stopwords=stopwords).generate(trump.lower())
wcClinton = WordCloud(max_font_size=40,stopwords=stopwords).generate(clinton.lower())
wcObama.to_file("obama1.png")
plt.figure()
plt.imshow(wcObama)
plt.axis("off")
plt.show()

wcTrump.to_file("trump1.png")
plt.figure()
plt.imshow(wcTrump)
plt.axis("off")
plt.show()

wcClinton.to_file("clinton1.png")
plt.figure()
plt.imshow(wcClinton)
plt.axis("off")
plt.show()

#################################################################################################
