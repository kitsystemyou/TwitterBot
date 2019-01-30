import os, sys, json
import tweepy
from tweepy import OAuthHandler
import yaml
from datetime import datetime
import random
import time

# tweepy config
cfg = yaml.load(open('api_key.yml', 'rt'))['twitter']
auth = OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
api = tweepy.API(auth)
print("start")

#set now time
t = datetime.now()
nowtime = str(t.hour)+"時"+str(t.minute)+"分"+str(t.second)+"秒"

def make_tweet(text):
    list = ["ふぁー","ふぁ","ふぁっ","ふぁーふぁ","ふぁぁ"]

    if "時間" in text or "タイム" in text or "time" in text:       #reply time
        tweet = random.choice(list)
        if "バジリスクタイム" in text:
            tweet += "水のようにぃいいいいいいいいいいやさぁあしぃくうううううううううううう\n"
            tweet += "花のようにぃいいいいいいいいいいいいいい激しぃくううううううううううううううううううううううううううううう"
        return tweet+str(nowtime)
    else:                                   #usual seagull bot
        length = random.randint(1,8)
        tweet =""
        for i in range(length):
                tweet += random.choice(list)
                if "群れ" in text:
                    for i in range(length):
                            tweet += random.choice(list)
        return tweet+"!"
        # return "Thank you for your replying me!@"+str(nowtime)


id_text_path = "id_text.txt"
with open(id_text_path) as f: # read most_latest_ID
    most_latest_ID = f.readline()
    print(most_latest_ID)

interval = 20 # interval of tweepy.Cursor
while True:
    c = 0
    for replies in tweepy.Cursor(api.mentions_timeline, since_id = most_latest_ID).items(): # catch mentions
        c+=1
        if c==1:
            most_latest_ID = replies.id

        print(replies.text, replies.entities["user_mentions"],replies.id)
        print()
        if "カモメbot" in replies.text:        #reply include the word or not
            tweet_all = make_tweet(replies.text)
            print(tweet_all)
            api.update_status(status=tweet_all, in_reply_to_status_id=replies.id, auto_populate_reply_metadata="True")

        print(most_latest_ID, replies.id)    # checking most_latest_ID whether updating or not
    print("complete checking replies")

    with open(id_text_path, mode="w") as f:  # write most_latest_ID
        f.write(str(most_latest_ID))

    time.sleep(interval)
