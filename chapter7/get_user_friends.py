# -*- coding: utf-8 -*-
'''
@author:Zhukun Luo
Jiangxi university of finance and economics
'''
import pandas as pd
import twitter
import time
import sys
from pandas.tests.io.parser import skiprows
consumer_key="G3wBU3xmr3O003cnNkgnr6Phg"
consumer_secret="jObdFcAPjFI1hMyftUFopUsTFZ4j1829A153RDsX7k8FncTuQz"
access_token="2396402040-c8ci1s6oqkCtNJB5CDPAksF36kvG5V040CAYXyy"
access_token_secret="AY2WJMcrYIUF9th033P3ELSyXE2JhbzC1PdMW6oNT1uin"
authorization=twitter.OAuth(access_token,access_token_secret,consumer_key,consumer_secret)
t=twitter.Twitter(auth=authorization,retry=True)
def get_friend(t,user_id):
    friends=[]
    cursor=-1#twitter的pagination对象分页
    while cursor !=0:
        try:
            results=t.friends.ids(user_id=user_id,cursor=cursor,count=5000)
            friends.extend([friend for friend in results["ids"]])
            cursor=results["next_cursor"]
            if len(friends)>=10000:
                break
        except TypeError as e:
            if results is None:
                print("你已达到你的api使用次数限制，请五分钟后再试！")
                sys.stdout.flush()
                time.sleep(5*60)           
            else:
                raise e
        except twitter.TwitterHTTPError as e:
            break
        finally:
            time.sleep(60)
    return friends
'''
.............................................构建网络..........................................................
'''
user=pd.read_csv("E://webJRE/ldmp/chapter7/dataset/twitter_user_info.csv")
friends={}
#for screen_name in relevent_users:
for user_id in user['userId']:
    friends[user_id]=get_friend(t, user_id) 
for user_id in friends:
    if len(friends[user_id])<0:  
        friends.popitem(user_id,friends[user_id])#移除不僵尸账号
#统计每个好友出现的次数
from collections import defaultdict
def count_friends(friends):#统计共同好友出现次数
    friend_count=defaultdict(int)
    for friend_list in friends.values():
        for friend in friend_list:
            friend_count[friend]+=1
    return friend_count
friend_count=count_friends(friends)
from operator import itemgetter#排序迭代器
best_friends=sorted(friend_count.items(),key=itemgetter(1),reverse=True)
while len(friends)<2:
    for user_id,count in best_friends:
        if user_id not  in best_friends:
            break
        friends[user_id]=get_friend(t, user_id)
    for friend in friends[user_id]:
        friend_count[friend]+=1
    best_friends=sorted(friend_count.items(),key=itemgetter(1),reverse=True)
import json
json.dump(friends,"dataset/friends.csv")
     
            