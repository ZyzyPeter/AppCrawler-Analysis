import urllib2
import urllib
import Po.Data
import requests

data=Po.Data.data()
values={'username':data.getUsername(),'password':data.getPassword()}
requestData=urllib.urlencode(values)
userAgent=data.getUseraAgent()
headers={'User-Agent':userAgent,
         'Referer':data.getReferer()}

class urlRequest:
    def __init__(self):
        self.__request=None
    def getRequest(self,url='http://www.appzapp.us/Service/listings.asmx/GetActivityDetails'
                   ,referer=data.getReferer()):
        headers = {
            "Content-type":"application/json; charset=utf-8",
            'User-Agent': userAgent,
                   'Referer':referer}
        self.__request = urllib2.Request(url, requestData, headers)
        return self.__request
    def getPageRequest(self):
        pass
    def getAppResquest(self):
        pass

if __name__ == "__main__":
    url = 'http://www.appzapp.us/Service/listings.asmx/GetActivityDetails'
    referer='http://www.appzapp.us/Index.html'
    params={
        'id': '20339720'
    }
    headers={
        "Content-type": "application/json; charset=utf-8",
        'User-Agent': userAgent,
        'Referer': referer
    }
    request=requests.get(url,params=params,headers=headers)
    print request.json()