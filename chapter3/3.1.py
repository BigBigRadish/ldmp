# -*- coding: utf-8 -*-
'''
@author:Zhukun Luo
Jiangxi university of finance and economics
'''
import pandas as pd
import numpy as np
data_filename='dataset/dicision trees sample.csv'
dataset=pd.read_csv(data_filename,parse_dates=["Date"])
dataset.columns=["Date","start","Visitor Team","visitorPts","Home Team","homePts","Score Type","OT?","Notes"]
#print(dataset.head(5))
print(dataset.ix[:5])
dataset["HomeWin"]=dataset["visitorPts"]<dataset["homePts"]
print(dataset["HomeWin"]);
dataset["HomeLastWin"]=""
dataset["VisitorLastWin"]=""
y_true=dataset["HomeWin"].values#numpy type
print(type(y_true))
from collections import defaultdict
won_last=defaultdict()
for index,row in dataset.iterrows():
    home_team =row ["Home Team"]
    visitor_team =row["Visitor Team"]
    won_last[home_team]=row["HomeWin"]
    won_last[visitor_team]=not row["HomeWin"]
    row["HomeLastWin"]=won_last[home_team]
    row["VisitorLastWin"]=won_last[visitor_team]
    dataset.ix[index]=row#ix更新每一行
print(dataset.ix[20:25])
#dataset.to_csv("1.csv")
from sklearn.tree import DecisionTreeClassifier  
from sklearn import cross_validation
clf =DecisionTreeClassifier(random_state=14)
x_previouswins=dataset [["HomeLastWin","VisitorLastWin"]].values
scores=cross_validation.cross_val_score(clf,x_previouswins,y_true,scoring='accuracy')
print("accuracy:{0:.1f}%".format(np.mean(scores)*100))