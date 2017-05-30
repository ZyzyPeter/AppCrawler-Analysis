import cookielib
import urllib2

import Po.Data
from Po import Data

data=Po.Data.data()
filename=data.getCookieFile()

class cookieJar(object):
    def __init__(self):
        self.__cookieJar=cookielib.MozillaCookieJar(filename)

    def getCookieJar(self):
        return self.__cookieJar

    def saveCookie(self,cookie):
        cookie.save(ignore_discard=True, ignore_expires=True)

    def loadCookie(self):
        cookie=self.__cookieJar.load(filename,ignore_discard=True,ignore_expires=True)
        return cookie
    def cookieSaver(self,url):
        cookieJar=self.__cookieJar
        handler=urllib2.HTTPCookieProcessor(cookieJar)
        opener=urllib2.build_opener(handler)
        response=opener.open(url)
        self.saveCookie(cookieJar)
        print response.read()

if __name__ == "__main__":
    cookieJar=cookieJar()
    data=Data.data()
    address=data.getAddress()
    cookieJar.cookieSaver(address)
