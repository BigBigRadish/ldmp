# -*- coding: utf-8 -*-
'''
@author:Zhukun Luo
Jiangxi university of finance and economics
'''
import numpy as np
from PIL import Image,ImageDraw,ImageFont
from skimage import transform as tf
from matplotlib import pyplot as plt
def create_captcha(text,shear=0,size=(100,24)):#单词，错切值，图片大小
    im=Image.new("L", size, "black")#初始化一个实例
    draw=ImageDraw.Draw(im)
    font=ImageFont.truetype(r'Coval-Book.otf', 22)#指定字体和大小
    draw.text((2,2), text, fill=1, font=font)
    image=np.array(im)
    affine_tf=tf.AffineTransform(shear=shear)
    image=tf.warp(image,affine_tf)
    return image/image.max()
image=create_captcha('GENE', shear=0.5)
plt.imshow(image,cmap='Greys')
plt.show()
        