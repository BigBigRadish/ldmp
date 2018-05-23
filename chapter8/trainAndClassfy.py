# -*- coding: utf-8 -*-
'''
@author:Zhukun Luo
Jiangxi university of finance and economics
'''
import numpy as np
import pybrain
from chapter8 import create_trainset
from chapter8.create_trainset import x_train,y_train,x,y,x_test,y_test
from pybrain.datasets import  SupervisedDataSet
import chapter8
training= SupervisedDataSet(x.shape[1],y.shape[1])
for i in range(x_train.shape[0]):
    training.addSample(x_train[i], y_train[i])
testing= SupervisedDataSet(x.shape[1],y.shape[1])
for i in range(x_test.shape[0]):
    training.addSample(x_test[i], y_test[i])
from pybrain.tools.shortcuts import buildNetwork
net= buildNetwork(x.shape[1],100,y.shape[1],bias=True)
from pybrain.supervised.trainers import BackpropTrainer
trainer=BackpropTrainer(net,training,learningrate=0.01,weightdecay=0.01)
trainer.trainEpochs(epochs=20)#固定运行20步
predictions=trainer.testOnClassData(dataset=testing)
from sklearn.metrics import f1_score
print("F-sore:{0:.2f}".format(*f1_score(y_test.argmax((axis=1))),predictions))

    
    