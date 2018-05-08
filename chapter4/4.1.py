# -*- coding: utf-8 -*-
'''
@author:Zhukun Luo
Jiangxi university of finance and economics
'''
import sys
import pandas as pd
import matplotlib.pyplot as pl
all_ratings=pd.read_csv(r"dataset/u.data",delimiter="\t" ,header=None)
all_ratings.columns=["userId","movieId","Rating","timeStamp"]
#print(all_ratings.ix[5])
ratings=all_ratings.pivot_table(index="userId",columns="movieId")
#print (ratings.head(5))
all_ratings["favorible"]=all_ratings["Rating"]>3
excise_ratings=all_ratings[all_ratings["userId"].isin(range(200))]
favorible_ratings=excise_ratings[excise_ratings["favorible"]]
favorible_reviews_by_users=dict((k,frozenset(v.values)) for k,v in favorible_ratings.groupby("userId")["movieId"])
#print(favorible_reviews_by_users) 
num_favorible_by_movie=excise_ratings[["movieId","favorible"]].groupby("movieId").sum()
print (num_favorible_by_movie.sort_values("favorible",ascending=False))
'''
.............................................Apriori algorithm...........................................
'''
frequent_itemsets={}#项集长度为键值，value为频繁项集
min_support=30#设置最小支持度为30
frequent_itemsets[1]=dict((frozenset((movie_id,)),#每一部电影的项集
                                            row["favorible"])
                                            for movie_id,row in num_favorible_by_movie.iterrows()
                                            if row["favorible"]>min_support)
from collections import defaultdict
def find_frequent_itemsets(favorible_reviews_by_users,k_1_itemsets,min_support):
    counts=defaultdict(int)
    for user,reviews in favorible_reviews_by_users.items():
        for itemset in k_1_itemsets:
            if itemset.issubset(reviews):
                for other_reviewed_movie in reviews-itemset:
                    current_superset=itemset|frozenset((other_reviewed_movie,))
                    counts[current_superset]+=1
    return dict([(itemset,frequency) for itemset,frequency in counts.items() if frequency >= min_support])

for k in range(2,20):
    cur_frequent_itemsets=find_frequent_itemsets(favorible_reviews_by_users,frequent_itemsets[k-1],min_support)
    frequent_itemsets[k]=cur_frequent_itemsets
    if len(cur_frequent_itemsets)==0:
        print("没有找到任何的频繁项集 {}".format(k))
        sys.stdout.flush()#及时将输出刷出到终端
        break
    else:
        print("发现{}个长度为{}的频繁项集".format(len(cur_frequent_itemsets),k))
        sys.stdout.flush()
del frequent_itemsets[1]
'''
..............................................抽取关联规则.......................................................

'''
candidate_rules=[]
for itemset_length,itemset_counts in frequent_itemsets.items():
    for itemset in itemset_counts.keys():
        for conclusion in itemset:
            premise=itemset-set((conclusion,))
            candidate_rules.append((premise,conclusion))
print (candidate_rules[:5])
'''
.............................................评估...............................................................abs
'''
