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
consumer_key="G3wBU3xmr3O003cnNkgnr6Phg"
consumer_secret="jObdFcAPjFI1hMyftUFopUsTFZ4j1829A153RDsX7k8FncTuQz"
access_token="2396402040-c8ci1s6oqkCtNJB5CDPAksF36kvG5V040CAYXyy"
access_token_secret="AY2WJMcrYIUF9th033P3ELSyXE2JhbzC1PdMW6oNT1uin"
authorization=twitter.OAuth(access_token,access_token_secret,consumer_key,consumer_secret)

output_filename="E://webJRE/ldmp/chapter6/dataset/twitter_data.json"

t=twitter.Twitter(auth=authorization)

output_file=codecs.open (output_filename,'a','utf-8') #codec好使用
search_results=t.search.tweets(q='python',count=1000)['statuses']
for tweet in search_results:
    if 'text' in tweet:
        output_file.write(json.dumps(tweet,ensure_ascii=False))
        output_file.write("\n\n")

#print(t.search_results)