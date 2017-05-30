# coding=utf-8
import mysql.connector
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
class Crud(object):
    def __init__(self, user='crawler', password='password', database='CrawlerData'):
        self.__user = user
        self.__password = password
        self.__database = database

    def execute(self, sqlQuery, params):
        connection = mysql.connector.connect(user=self.__user, password=self.__password, database=self.__database)
        cursor = connection.cursor()
        cursor.execute(sqlQuery, params)
        connection.commit()
        print 'Data saved successfully'
        cursor.close()
        connection.close()

    def search(self):
        connection = mysql.connector.connect(user=self.__user, password=self.__password, database=self.__database)
        cursor = connection.cursor()
        cursor.execute("select * from appdata")
        records=cursor.fetchall()
        cursor.close()
        connection.close()
        return records

