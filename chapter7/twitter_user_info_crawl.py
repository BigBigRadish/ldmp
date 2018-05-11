# -*- coding: utf-8 -*-
'''
@author:Zhukun Luo
Jiangxi university of finance and economics
'''
from __future__ import unicode_literals
import os
import json
import twitter
import codecs
import pandas as pd
consumer_key="G3wBU3xmr3O003cnNkgnr6Phg"
consumer_secret="jObdFcAPjFI1hMyftUFopUsTFZ4j1829A153RDsX7k8FncTuQz"
access_token="2396402040-c8ci1s6oqkCtNJB5CDPAksF36kvG5V040CAYXyy"
access_token_secret="AY2WJMcrYIUF9th033P3ELSyXE2JhbzC1PdMW6oNT1uin"
authorization=twitter.OAuth(access_token,access_token_secret,consumer_key,consumer_secret)
t=twitter.Twitter(auth=authorization,retry=True)
data_filename="E://webJRE/ldmp/chapter7/dataset/twitter_user_info.csv"
original_users=[]
tweets=[]
user_ids={}
search_results=t.search.tweets(q="chinese",count=10000)["statuses"]
for tweet in search_results:
    if 'text' in tweet:
        original_users.append(tweet['user']['screen_name'])
        user_ids[tweet['user']['screen_name']]=str(tweet['user']['id'])
        tweets.append(tweet['text'])
print(user_ids)
user_info=pd.DataFrame(list(user_ids.items()),columns=['userName','userId'])#dict转list
print(user_info)
user_info.to_csv(data_filename,mode='a')