# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:07:21 2016

@author: Tanvi
"""
from textblob import TextBlob
import json
import os
import numpy as np

jsonFiles = []
polResult,polTotal = [],[]
subResult,subTotal = [],[]

polObama,subObama = [],[]
polTrump,subTrump = [],[]
polClinton,subClinton=[],[]

obama = ''
trump = ''
clinton = ''
#Sentiment Analysis for those locations
jsonFiles = []
polObama,subObama = [],[]
polTrump,subTrump = [],[]
polClinton,subClinton=[],[]
obama,trump,clinton = '','',''
filepath = 'C:/Users/Tanvi/Downloads/Project/json1'
for files in os.listdir(filepath):
    if files.endswith(".json") and ('Obama' not in files) and ('Trump' not in files ) and ('Clinton' not in files):
        jsonFiles.append(files)
os.chdir(filepath)
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)
for filename in jsonFiles:
    infile = open(filename).read()
    content = json.loads(infile)
    #to be run for the number of tweets collected per json file   
    
    for i in range(len(content)):        
        token = content[i]['text']
        
        if 'obama' in token.lower():
            token = strip_non_ascii(token)
            obama += token + '\n'
            senObama = TextBlob(token)
            polObama.append(senObama.sentiment.polarity)
            subObama.append(senObama.sentiment.subjectivity)
        elif ('trump' or 'donald') in token.lower():
            token = strip_non_ascii(token)
            trump += token + '\n'
            senTrump = TextBlob(token)
            polTrump.append(senTrump.sentiment.polarity)
            subTrump.append(senTrump.sentiment.subjectivity)
        elif ('clinton' or 'hillary') in token.lower():
            token = strip_non_ascii(token)
            clinton += token + '\n'
            senClinton = TextBlob(token)
            polClinton.append(senClinton.sentiment.polarity)
            subClinton.append(senClinton.sentiment.subjectivity)
    
print('Total number of tweets collected:{}\n'.format(len(jsonFiles)*len(content)))
print('Polarity:\nObama:{} Trump:{} Clinton:{}\n'.format(np.mean(polObama),np.mean(polTrump),np.mean(polClinton)))
print('Subjectivity:\nObama:{} Trump:{} Clinton:{}\n'.format(np.mean(subObama),np.mean(subTrump),np.mean(subClinton)))
print('No. of tweets pertaining to candidates:\nObama:{} Trump:{} Clinton:{}\n'.format(len(subObama),len(subTrump),len(subClinton)))


#stopwords = nltk.corpus.stopwords.words('english')
#stopwords.append(u'https')
#stopwords.append(u'http')
#stopwords.append(u'rt')
#
#wcObama = WordCloud(max_font_size=40,stopwords=stopwords).generate(obama.lower())
#wcTrump = WordCloud(max_font_size=40,stopwords=stopwords).generate(trump.lower())
#wcClinton = WordCloud(max_font_size=40,stopwords=stopwords).generate(clinton.lower())
#wcObama.to_file("obama1.png")
#plt.figure()
#plt.imshow(wcObama)
#plt.axis("off")
#plt.show()
#
#wcTrump.to_file("trump1.png")
#plt.figure()
#plt.imshow(wcTrump)
#plt.axis("off")
#plt.show()
#
#wcClinton.to_file("clinton1.png")
#plt.figure()
#plt.imshow(wcClinton)
#plt.axis("off")
#plt.show()