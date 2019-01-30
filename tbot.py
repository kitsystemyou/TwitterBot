# coding: UTF-8

import twitter
import time
import datetime
import random

access_token = "access_token"
access_token_secret = "acess_token_secret"
api_key = "api_key"
api_secret = "api_secret"

auth = twitter.OAuth(access_token, access_token_secret, api_key, api_secret)
t = twitter.Twitter(auth = auth)

t_userstream = twitter.TwitterStream(auth=auth,domain='userstream.twitter.com')

def tweet (tw):
    tweet = "@"+msg['user']['screen_name']+str(tw)
    t.statuses.update(status=tweet,in_reply_to_status_id=msg["id"])
    print("Repried")

for msg in t_userstream.user():
 #TLにリプライでTWITTE_IDが含まれてたら分岐



 if "in_reply_to_screen_name" in msg:   #exist or not ->index
    if msg["in_reply_to_screen_name"] == ("kit_systemyou"):
        if msg["text"].find("時間")>-1 or msg["text"].find("タイム")>-1:
            n = datetime.datetime.now().strftime('%-H %-M %-S').split() #('%Y/%m/%d %H:%M:%S')
            now = "ふぁー！\n" + n[0]+"時"+n[1]+"分"+n[2]+"秒"
            if msg["text"].find("バジリスクタイム")>-1: #hidden command
                now += "水のようにぃいいいいいいいいいいやさぁあしぃくうううううううううううう\n"
                now += "花のようにぃいいいいいいいいいいいいいい激しぃくううううううううううううううううううううううううううううう"
            else:
                pass
            tweet(now)

        elif msg["text"].find("カモメbot")>-1:
            li = ["ふぁー","ふぁ","ふぁっ","ふぁーふぁ","ふぁぁ"]
            num = random.randint(1,8)
            fa = ""
            for i in range(num):
                fa += random.choice(li)
            fa +="!"
            now = fa
            tweet(now)

        """tweet = "@"+msg['user']['screen_name']+str(now)
        t.statuses.update(status=tweet,in_reply_to_status_id=msg["id"])
        print("Repried")"""
