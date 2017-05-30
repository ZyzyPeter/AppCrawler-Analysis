# coding=utf-8
import Crud

from Util import Matcher
from Po import Date

crud = Crud.Crud()
matcher = Matcher.Matcher()
dateDict=Date.Date()
monthDict=dateDict.getMonthDict()

class DataFormater(object):
    def __init__(self):
        pass

    def dataForm(self):
        records = crud.search()
        appList = []
        for app in records:
            appData = {}
            appData['name'] = app[1]
            appData['id'] = app[0]
            appData['hits'] = int(app[2])
            appData['like']=int(app[3])
            appData['url']=app[4]
            appData['type']=app[5]
            appList.append(appData)
        return appList
