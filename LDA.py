# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 08:52:43 2016

@author: Tanvi
"""
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora
import gensim

tokenizer = RegexpTokenizer(r'\w+')
twitter_words= ['https','co','http','rt','RT','u','t','amp',]
en_stop = get_stop_words('en')+twitter_words
p_stemmer = PorterStemmer()
kywrds = ['Obama','Trump','Clinton']

for wrd in kywrds:
    infile = open('C:\\Users\\Tanvi\\Downloads\\Project\\json\\{}Tweets.txt'.format(wrd)).readlines()
    texts = []

    for i in infile:
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)
        stopped_tokens = [i for i in tokens if not i in en_stop]
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        texts.append(stemmed_tokens)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=20, id2word = dictionary, passes=20)
    print(ldamodel.print_topics())
# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=20, id2word = dictionary, passes=20)
ldamodel.print_topics()


