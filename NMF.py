import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import decomposition
import json
import os
import re

jsonFiles = []
polObama,subObama = [],[]
polTrump,subTrump = [],[]
polClinton,subClinton=[],[]
obama,trump,clinton = '','',''
obamaCorpus,trumpCorpus,clintonCorpus=[],[],[]
jsonObamaFiles,jsonTrumpFiles,jsonClintonFiles = [],[],[]

def parse_text(text): #funtion to clean tweet data
    text = re.sub(r"http\S+", "", text) # removes hyperlinks
    text = re.sub(r"@\S+", "", text)    # removes user names
    text = re.sub(r"#\S+", "", text)    # removes hash tags
    text = re.sub(r'[-.#/?@??!,":;()]',' ',text.lower().replace('\n', ' '))
    text = re.sub(r'[\']','',text) # removes ' without adding space so that don't becomes dont and not don t
    text = re.sub(r"\d", "", text)      # removes digits
    text = re.sub(r'https|2016|hillary|clinton|hillaryclinton|donald|trump|Trump|donaldtrump|obama2016|barackobama|barack|obama|https|2016|rt','',text)
    text = ' '.join(text.split())       # removes any additional white spaces
    return text

os.chdir('C:/Users/Tanvi Mehta/Downloads/Twitter/Project/Project/json')
jsonObamaFiles,jsonObamaFiles,jsonClintonFiles=[],[],[]
for files in os.listdir('../json'):
    if files.endswith('json') and 'Obama' in files:
        jsonObamaFiles.append(files)
    elif files.endswith('json') and 'Trump' in files:
        jsonTrumpFiles.append(files)
    elif files.endswith('json') and 'Clinton' in files:
        jsonClintonFiles.append(files)
for filename in jsonObamaFiles:
    infile = open(filename).read()
    content = json.loads(infile)
    for i in range(len(content)):        
        tweet = parse_text(content[i]['text'])
        obama += tweet + '\n'
    obamaCorpus.append(obama)
    obama=''
for filename in jsonTrumpFiles:
    infile = open(filename).read()
    content = json.loads(infile)
    for i in range(len(content)):        
        tweet = parse_text(content[i]['text'])
        trump += tweet + '\n'
    trumpCorpus.append(trump)
    trump = ''
for filename in jsonClintonFiles:
    infile = open(filename).read()
    content = json.loads(infile)
    for i in range(len(content)):        
        tweet = parse_text(content[i]['text'])
        clinton += tweet + '\n'
    clintonCorpus.append(clinton)
    clinton=''

def corp(corpText):
    dtm = vectorizer.fit_transform(corpText) #obamaCorpus is a list of files having tweets.
    print(dtm.shape)
    
    num_terms = len(vectorizer.vocabulary_)
    terms = [""] * num_terms
    for term in vectorizer.vocabulary_.keys():
    	terms[ vectorizer.vocabulary_[term] ] = term
    
    num_topics = 20
    num_top_words = 10
    clf = decomposition.NMF(n_components = num_topics, random_state=2)
    doctopic = clf.fit_transform(dtm)
    
    topic_words = []
    for topic in clf.components_:
        word_idx = np.argsort(topic)[::-1][0:num_top_words]
        #print (word_idx)    
        topic_words.append([terms[i] for i in word_idx])
    
    for t in range(len(topic_words)):
        print("Topic {}: {}".format(t, ' '.join(topic_words[t][:20])))
    topic_words = []
    
vectorizer = TfidfVectorizer(stop_words='english', min_df=2)
corp(obamaCorpus)
corp(trumpCorpus)
corp(clintonCorpus)