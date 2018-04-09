# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 15:19:47 2016

@author: Tanvi
"""


from twython import Twython
import json
import time
import random


tweets = []
x = random.randrange(5,10)

class MyStreamer(Twython):
    '''our own subclass of TwythonStremer'''

    # overriding
    def on_success(self, data):
        if 'text' in data:
            if data['lang'] == 'en' and 'trump' in data['text'].lower():
                tweets.append(data)
                print('received tweet #', len(tweets), data['text'][:100].encode('utf-8'))
                
        if len(tweets) >= 200:
            self.store_json()
            self.disconnect()
        
    # overriding
    def on_error(self, status_code, data):
        print(status_code, data)
        self.store_json()        
        self.disconnect()

    def store_json(self):
        with open('tweet_stream_{}_{}.json'.format(kywrds[wrd], i), 'w') as f:
            json.dump(tweets, f, indent=4)

locations = ['31.968599,-99.901813,385mi',
             '-74,40,-73,41',
             '-96.89,32.66,-96.67,32.87',
             '-118.79,32.64,-116.97,34.90',
             '-87.66,41.83,-87.63,42.01',
             '-77.03,38.86,-76.97,38.94',
             '-85.02,33.37,-83.81,34.22']
if __name__ == '__main__':

    with open('tanvi_twitter_credentials.json', 'r') as f:
        credentials = json.load(f)

    # create your own app to get consumer key and secret
    CONSUMER_KEY = credentials['CONSUMER_KEY']
    CONSUMER_SECRET = credentials['CONSUMER_SECRET']
    ACCESS_TOKEN = credentials['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']    
    kywrds=['CA','NYC','DAL','LA','CHI','DC','ATL']
    for wrd in range(7):
        for i in range(1,11):
            stream  = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)            
            stream.search(q='trump',geocode=locations[wrd],count=100)
            tweets=[]
            time.sleep(x)

        
        

    
        