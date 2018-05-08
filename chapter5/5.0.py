# -*- coding: utf-8 -*-
'''
@author:Zhukun Luo
Jiangxi university of finance and economics
'''
from collections import defaultdict
import pandas as pd
filename ="dataset/adult.data"
dataset=pd.read_csv(filename,header=None,names=["age","workClass","fnlwgt","education","education-Num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country","Earning-Raw"])
#print (dataset.ix[:10])
dataset.dropna(how='all',inplace=True)
print(dataset.columns)
'''
..............................................General feature create.............................................
'''
import numpy as np
x=np.arange(30).reshape((10,3))
x[:,1]=1
from sklearn.feature_selection import VarianceThreshold#处理低方差的某一列
vt =VarianceThreshold()
xt=vt.fit_transform(x)
print(vt.variances_)
'''
..............................................select best feature......................................................
'''
#选取单个特征,chi2衡量相关性
x =dataset[["age","capital-gain","education-Num","capital-loss","hours-per-week"]].values
y=(dataset["Earning-Raw"]==' >50K').values
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
transformer=SelectKBest(score_func=chi2,k=3)
xt_chi2=transformer.fit_transform(x,y)#返回特征
print(transformer.scores_)
#pearson corrolections
from scipy.stats import pearsonr
def multivariate_pearsonr(x,y):
    scores,pvalue=[],[]
    for column in range(x.shape[1]):#遍历每一列
        cur_score,cur_p=pearsonr(x[:,column],y)
        scores.append(abs(cur_score))
        pvalue.append(cur_p)
    return (np.array(scores),np.array(pvalue))
transformer= SelectKBest(score_func=multivariate_pearsonr,k=3)
xt_pearsonr=transformer.fit_transform(x,y)
print(transformer.scores_)
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score
clf=DecisionTreeClassifier(random_state=14)
scores_chi2=cross_val_score(clf,xt_chi2,y,scoring='accuracy')
scores_pearson=cross_val_score(clf,xt_pearsonr,y,scoring="accuracy")
print(scores_chi2,scores_pearson)
'''
.................................................create new feature.................................................
'''
#onehot encoding
#converters=defaultdict(float)
def convert_number(x):#特征处理
    try:
        return float(x)
    except ValueError:
        return np.nan
converters=defaultdict(convert_number)
converters[1558]=lambda x:1 if x.strip()=='ad.' else 0
ads=pd.read_csv("dataset/ad.txt",header=None,converters=converters)
x=ads.drop(1558,axis=1).values
y=ads[1558]
print(x)
print(y)
'''
..................................................PCA..................................................................
'''
from sklearn.decomposition import PCA
pca=PCA(n_components=5)#挑选最好的5个特征
xd=pca.fit_transform(x)
np.set_printoptions(precision=3,suppress=True)
print(pca.explained_variance_ratio_)
clf=DecisionTreeClassifier(random_state=14)
scores_reduced=cross_val_score(clf,xd,y,scoring='accuracy')
'''
............................................create transformer.................................................
'''
