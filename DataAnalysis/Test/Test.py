import numpy as np
import pandas as pd
import pylab as pl
import json
import matplotlib.pyplot as plt
from Dao import DataFormater
from pandas import DataFrame, Series
from Dao import Crud

path = r'D:\study\python ide\ML\pydata-book\pydata-book-master\ch02\usagov_bitly_data2012-03-16-1331923249.txt'

records = [json.loads(line) for line in open(path)]

time_zone = [rec['tz'] for rec in records if 'tz' in rec]


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


dataFormater=DataFormater.DataFormater()
records=dataFormater.dataForm()
frame=DataFrame(records)

counts=frame['type'].value_counts()
print counts


