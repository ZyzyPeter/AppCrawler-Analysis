# coding=utf-8
from Dao import DataFormater

import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
import sys


reload(sys)
sys.setdefaultencoding('utf-8')
dataFormater=DataFormater.DataFormater()

if __name__ == "__main__":
    app_list=dataFormater.dataForm()#获取信息
    frame=DataFrame(app_list,columns=['id','name','hits','like','url','type']).sort_values(by='name')
    name_duplicated=frame['name'].duplicated()#创建一个判断名字是否重复的布尔型Series
    frame=frame[name_duplicated==False]#去除重复的app
    frame.to_csv('File/app_frame.csv')
    app_types=frame['type'].unique()#获取所有的app类型
    app_hits_sum=[]
    app_likes_sum=[]
    for app_type in app_types:
        app_hits_sum.append(frame[frame['type'].isin([app_type])]['hits'].sum())
        #计算每个app类型的hits的总数
        app_likes_sum.append(frame[frame['type'].isin([app_type])]['like'].sum())
        # 计算每个app类型的like的总数
    types_data=DataFrame({'hits':app_hits_sum,'like':app_likes_sum},index=app_types,columns=['hits','like']).sort_values(by='hits',ascending=True)
    # 将hits与app类型格式化并进行排序
    types_data.index.name='types'
    for column in types_data.columns:
        types_data[column]=types_data[column]/(types_data[column].sum()).astype(float)
    #规整数据，计算每个app类型的hits和like占总数的百分比
    types_data.to_csv('File/types_data.csv')#输出数据
    figure,axes=plt.subplots(1,1)
    types_data.plot(kind='barh',figsize=(20,20),title='Hits and likes\' percentage of app types')
    plt.savefig('img/hits_and_likes_pct',dpi=400,bbox_inches='tight')
    plt.show()