from Util import Matcher
from selenium import webdriver

matcher=Matcher.Matcher()
class UrlManager(object):
    def __init__(self):
        self.newUrls=set()
        self.oldUrls=set()
        self.driver=webdriver.PhantomJS(executable_path=r'D:\study\python ide\phantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe')

    def addNewUrl(self, url):
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)
        if url is None:
            return

    def addNewUrls(self, newUrls):
        if newUrls is None or len(newUrls)==0:
            return
        for url in newUrls:
            self.addNewUrl(url)

    def hasNewUrl(self):
        return len(self.newUrls)!=0

    def getNewUrl(self):
        newUrl=self.newUrls.pop()
        self.oldUrls.add(newUrl)
        return newUrl