addressDict={
    '6010':'Navigat',
    '6014':'Games',
    '6012':'LifeStyle',
    '6011':'Music',
    '6003':'Travel',
    '6016':'Entertain',
    '6005':'Social',
    '6009':'News',
    '6018':'Books',
    '6017':'Education',
    '6002':'Utilities',
    '6008':'Fotographie',
    '6013':'Healthcare and Fitness',
    '6020':'Medical',
    '6007':'Productivity',
    '6006':'Reference',
    '6004':'Sport',
    '6015':'Finance',
    '6001':'Weather',
    '6000':'Business'
}

class data:
    def __init__(self):
        self.__username='zyzy'
        self.__password='zyzy19971222'
        self.__address='http://www.appzapp.us/New.html#popFilter:Popular|priceFilter:All|activityFilter:Price'
        self.__userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        self.__cookieFile=r'..\File\Cookie\Cookie'
        self.__referer=r'http://www.appzapp.us/Index.html'
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getAddress(self):
        return self.__address
    def getUseraAgent(self):
        return self.__userAgent
    def getCookieFile(self):
        return self.__cookieFile
    def getReferer(self):
        return self.__referer
    def getTypeDict(self):
        return addressDict
