# coding=utf-8
from Dao import DataFormater

import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt

dataFormater=DataFormater.DataFormater()
if __name__ == "__main__":
    app_list=dataFormater.dataForm()#获取信息
    frame=DataFrame(app_list,columns=['id','name','hits','like','url','type']).sort_values(by='name')
    name_duplicated=frame['name'].duplicated()#创建一个判断名字是否重复的布尔型Series
    frame=frame[name_duplicated==False]#去除重复的app
    trans_frame=frame[frame['like']>0]#去掉like等于0的app数据
    coefficient_of_hits_and_likes=trans_frame['hits'].corr(trans_frame['like'])#计算app的hits与like的相关系数
    data=trans_frame.drop(['id','name','url','type'],axis=1)
    figure,axes=plt.subplots(1,1)
    pd.scatter_matrix(data,diagonal='kde',c='k',alpha=0.3,figsize=(10,5))#生成散布图
    print coefficient_of_hits_and_likes#打印相关系数
    plt.savefig('img/scatter_plot_about_hit_and_likes.png', dpi=400, bbox_inches='tight',title='Association of hits and likes')
    plt.show()






