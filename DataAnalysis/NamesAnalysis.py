# coding=utf-8
from Dao import DataFormater

from collections import defaultdict
from matplotlib import pyplot as plt
from pandas import DataFrame
import numpy as np
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
dataFormater = DataFormater.DataFormater()


def word_set(name_list, method='set'):
    single_abandom = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    if method is 'set':
        words = set()
        for name in name_list:
            if name is None or name is np.nan:
                continue
            for word in name:
                if word is None or word is np.nan:
                    continue
                for character in single_abandom:
                    word = word.replace(character, '')
                words.add(word)
        return words
    elif method is 'list':
        words = []
        for name in name_list:
            for word in name:
                words.append(word)
        return words
        # 统计词汇函数


def frame_produced():
    app_list = dataFormater.dataForm()  # 获取信息
    app_frame = DataFrame(app_list, columns=['id', 'name', 'hits', 'like', 'url', 'type']).sort_values(by='name')
    name_duplicated = app_frame['name'].duplicated()  # 创建一个判断名字是否重复的布尔型Series
    app_frame = app_frame[name_duplicated == False]  # 去除重复的app
    return app_frame
    # 用收集的数据生成一个DataFrame


def save_file(file_to_save=None, filename='not_defined', method='file'):
    file_path = 'File/'
    img_path = 'img/'
    file_tail = '.csv'
    img_tail = '.png'
    method_type = {
        'img': img_path + filename + img_tail,
        'file': file_path + filename + file_tail
    }
    kw = {
        'img': {
            'dpi': 400,
            'bbox_inches': 'tight'
        },
        'file': {
        }
    }
    if method == 'file':
        file_to_save.to_csv(method_type[method], **kw[method])
    elif method == 'img':
        plt.savefig(method_type[method], **kw[method])
        # 自定义保存方法


def word_abandom(words_set):
    abandom_form = ('&', '-', '.', '?', ' ')
    for word in abandom_form:
        if word in words_set:
            words_set.remove(word)
    return words_set
    # 抛弃特殊字符的函数


def word_counter(word_list):
    word_counts = defaultdict(int)
    for word in word_list:
        word_counts[word] += 1
    return word_counts
    # 词语频率统计函数


def word_weight_counter(appframe):
    word_weight = defaultdict(int)
    for app_index in appframe.index:
        for word in appframe.ix[app_index]['name']:
            word_weight[word] += appframe.ix[app_index]['hits']
    return word_weight


if __name__ == "__main__":
    frame = frame_produced()
    frame['name'] = frame['name'].map(
        lambda x: re.split(r' |,|&|;|\\|\*|\+|\(|\)|\.|:|\?|\"|\'|\»|\«|\-', x.lower().replace('appzapp - ', '')))
    # 将app名字的前缀AppZapp去掉,并将名字的词语成分切出来
    frame = frame[(frame['hits'] == 0) == False]  # 去除点击量为0的app
    frame = frame.sort_values(by='hits', ascending=False)
    words = word_abandom(word_set(frame['name']))  # 创建一个词语集，包含所有的app名字中的词语且不重复,并且抛弃掉一些没有意义的词语
    word_list = word_set(frame['name'], method='list')  # 创建一个词语表,包含所有的app名字中的词语
    word_frequency = word_counter(word_list)  # 统计每个词出现的次数
    word_weight = word_weight_counter(frame)  # 统计每个词对应的点击量的权重
    word_frame = DataFrame \
            ({
            'weight': 0,
            'frequency': 0,
            'weight_pct': 0,
            'frequency_pct': 0}
            , columns=['weight', 'frequency', 'weight_pct', 'frequency_pct'], index=[word for word in words])
    # 创建一个词语计数表
    word_frame.index.name = 'word'
    for key, value in word_frequency.iteritems():
        if key in words:
            word_frame.ix[key]['frequency'] = value
    # 把词频记入计数表
    frequency_counts = word_frame['frequency'].value_counts()
    # 计算词频的频率，以便于区分低频词
    for key, value in word_weight.iteritems():
        if key in words:
            word_frame.ix[key]['weight'] = value
    # 把每个词获得的点击量记入计数表
    word_frame['hits'] = word_frame['weight']

    '''word_frame = pd.read_csv('File/word_frame.csv',index_col='word')'''

    word_frame = word_frame[(word_frame['frequency'] < 10) == False].dropna()
    # 去掉词频小于10的词
    word_frame['weight'] = (word_frame['hits'] / word_frame['frequency']).astype(float)
    # 计算出权数并记入权数列
    word_frame['weight_pct'] = word_frame['weight'] / (word_frame['weight'].sum()).astype(float)
    # 计算出每个词的权数百分比
    word_frame['frequency_pct'] = word_frame['frequency'] / (word_frame['frequency'].sum()).astype(float)
    # 计算出每个词的频率百分比
    word_frame = word_frame.sort_values(by='weight', ascending=False)
    # 将词语信息按照词的权数排序
    print word_frame
