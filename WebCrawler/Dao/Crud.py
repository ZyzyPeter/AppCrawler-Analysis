# coding=utf-8
import mysql.connector

class Crud(object):
    def __init__(self):
        self.__user ='crawler'
        self.__password ='password'
        self.__database = 'CrawlerData'

    def execute(self, sqlQuery,params) :
        connection = mysql.connector.connect(user=self.__user, password=self.__password, database=self.__database)
        cursor = connection.cursor()
        cursor.execute(sqlQuery, params)
        connection.commit()
        print 'Data saved successfully'
        cursor.close()
        connection.close()


