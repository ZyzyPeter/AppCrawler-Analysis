# coding=utf-8
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
import struct
import pandas as pd
import json

wordfile=open('../File/word_list.txt','r')
words=wordfile.read()
wordfile.close()
backimg=imread("../img/Apple.jpg")

#导入一张图片背景
wc = WordCloud(background_color="white", #背景颜色
max_words=2000,# 词云显示的最大词数
mask=backimg,#设置背景图片
stopwords=STOPWORDS.add("said"),
max_font_size=40, #字体最大值
random_state=42)#词云包api
wc.generate(words)#设置词与词频

image_colors = ImageColorGenerator(backimg)#从背景图片生成颜色值

plt.imshow(wc)#显示图片
plt.axis('off')#关闭坐标轴
plt.show()
wc.to_file('../img/word_frequency_cloud.png')