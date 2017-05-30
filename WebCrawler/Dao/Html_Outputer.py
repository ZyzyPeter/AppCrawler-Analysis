# coding=utf-8
import Crud
crud=Crud.Crud()
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collectData(self, newData):
        if newData is None:
            return
        if newData is 'pageLink':
            return
        self.datas.append(newData)

    def outputHtml(self,type):
        sqlQuery=('INSERT INTO appdata'
                  '(id, AppName, Hits, Likes, Url, Type)'
                  'VALUES (%s, %s, %s, %s, %s, %s)')
        if len(self.datas)!=0:
            data=self.datas.pop()
            url=data.get('url')
            name=data.get('name')
            hits=data.get('hits')
            likes=data.get('likes')
            params=('0', name, hits, likes, url, type)

            crud.execute(sqlQuery,params)
