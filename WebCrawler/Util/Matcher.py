import re

typeMatcher={
    'appLink':r'/App/.+\.html',
    'pageLink':r'http://www.appzapp.us/New.html#popFilter:Popular|priceFilter:All|activityFilter',
    'price':r'[0-9]+\.[0-9]{2}',
    'timeNode':r'(alt )?activity',
    'notRootUrl':r'http://www.appzapp.us/New.html#.+',
    'appName':'',
    'updateTime':'',
    'priceBeforUpdate':'',
    'priceAfterUpdate':''
}

class Matcher(object):
    def getPattern(self,type):
        regex=typeMatcher.get(type)
        return re.compile(regex)