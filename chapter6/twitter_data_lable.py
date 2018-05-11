# -*- coding: utf-8 -*-
'''
@author:Zhukun Luo
Jiangxi university of finance and economics
'''
from __future__ import unicode_literals
import json
import codecs
import os
input_filename="E://webJRE/ldmp/chapter6/dataset/twitter_data.json"
output_label_file="E://webJRE/ldmp/chapter6/dataset/twitter_data_label.json"
ouput_file=codecs.open(input_filename)
tweets=[]
for line in ouput_file:
    if len(line.strip())==0:
        continue
    tweets.append(json.loads(line))
lables=[]
if os.path.exists(output_label_file):
    lable_file=codecs.open(output_label_file)
    lables=json.loads(lable_file)
def get_next_tweet():
    return tweets[len(lables)]['text']
lable_file=codecs.open(output_label_file,"w")
json.dump(lables,lable_file)

