import mysql.connector

class Connection:
    def __init__(self,user='crawler',password='password',database = 'CrawlerData'):
        self.__user = user
        self.__password = password
        self.__database = database
        self.__conn = mysql.connector.connect(user=user, password=password, database=database)

    def getConnection(self):
        return self.__conn
    def getCursor(self):
        return self.__conn.cursor()