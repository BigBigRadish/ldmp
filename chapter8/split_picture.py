# -*- coding: utf-8 -*-
'''
@author:Zhukun Luo
Jiangxi university of finance and economics
'''
from skimage.measure import label, regionprops
from matplotlib import pyplot as plt
from IPython.core.pylabtools import figsize
from create_captcha import  image
def split_image(image):
    labeled_image=label(image>0)#连续区域非0表示
    subimage=[]#存取小图片
    for region in regionprops(labeled_image):#遍历连续区域，获取连续区域起始与结束坐标
        start_x,start_y,end_x,end_y=region.bbox
        subimage.append(image[start_x:end_x,start_y:end_y])
    if len(subimage)==0:
        return [image,]
    return subimage
subimage=split_image(image)
f,axes=plt.subplots(1,len(subimage),figsize=(10,3))
for i in range(len(subimage)):
    plt.show(axes[i].imshow(subimage[i],cmap="gray"))
   

        