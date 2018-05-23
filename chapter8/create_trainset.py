# -*- coding: utf-8 -*-
'''
@author:Zhukun Luo
Jiangxi university of finance and economics
'''
import numpy as np
from chapter8.create_captcha import create_captcha
from chapter8.split_picture import split_image
from matplotlib import pyplot as plt
from sklearn.utils import check_random_state
from sklearn.preprocessing import OneHotEncoder
random_state=check_random_state(14)
letters=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
shear_values=np.arange(0,0.5,0.05)
def generate_sample(random_state=None):
    random_state=check_random_state(random_state)
    letter=random_state.choice(letters)
    shear=random_state.choice(shear_values)
    return create_captcha(letter,shear=shear,size=(20,20)),letters.index(letter)
image,target=generate_sample(random_state)
plt.imshow(image,cmap='Greys')
plt.show()
print("The target for this image is :{0}".format(target))
dataset,targets=zip(*(generate_sample(random_state) for i in range(3000)))
datset= np.array(dataset,dtype='float')
targets= np.array(targets)
onehot=OneHotEncoder()
y= onehot.fit_transform(targets.reshape(targets.shape[0],1))
y= y.todense()
from skimage.transform import resize
dataset=np.array([resize(split_image(sample)[0],(20,20)) for sample in dataset])
x= dataset.reshape((dataset.shape[0],dataset.shape[1]*dataset.shape[2]))
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.9)