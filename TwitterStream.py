
from twython import TwythonStreamer
from datetime import datetime
import json
import time
import random


tweets = []
x = random.randrange(5,10)
dt = str(datetime.now().time())[:8].maketrans('_',':')
kywrds=['Obama','Trump','Clinton']
class MyStreamer(TwythonStreamer):
    '''our own subclass of TwythonStremer'''

    # overriding
    def on_success(self, data):
        if 'text' in data:
            if data['lang'] == 'en':
                tweets.append(data)
                print('received tweet #', len(tweets), data['text'][:100].encode('utf-8'))
                
        if len(tweets) >= 200:
            self.store_json()
            self.disconnect()
        
    # overriding
    def on_error(self, status_code, data):
        #print status_code, data
        self.store_json()        
        self.disconnect()

    def store_json(self):
        with open('tweet_stream_{}_{}_{}.json'.format(dt, wrd, i), 'w') as f:
            json.dump(tweets, f, indent=4)

if __name__ == '__main__':

    with open('tanvi_twitter_credentials.json', 'r') as f:
        credentials = json.load(f)

    # create your own app to get consumer key and secret
    CONSUMER_KEY = credentials['CONSUMER_KEY']
    CONSUMER_SECRET = credentials['CONSUMER_SECRET']
    ACCESS_TOKEN = credentials['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']    
    for wrd in kywrds:
        for i in range(1,51):
            stream  = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)            
            stream.statuses.filter(track=wrd)
            tweets=[]
            time.sleep(x)

        
        

    
        