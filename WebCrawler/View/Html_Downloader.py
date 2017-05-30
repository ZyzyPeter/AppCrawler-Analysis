# coding=utf-8
import urllib2
import requests
from flask import json
from Po import Data
from Util import Matcher
import Request
import Cookie

cookieJar=Cookie.cookieJar()
urlRequest=Request.urlRequest()
matcher=Matcher.Matcher()
data=Data.data()

class HtmlDownloader(object):
    def __init__(self):
        self.__response=None

    def download(self, newUrl):
        if newUrl is None:
            return None
        request=urlRequest.getRequest(url=newUrl)
        try:
            response=urllib2.urlopen(request)
            return response.read()
        except:
            return

    def downloadPageUrl(self,pageNumber,typeNumber):
        url = 'http://www.appzapp.us/Service/listings.asmx/GetGenreListing'
        params = {'genre':typeNumber,
                  'priceFilter':'All',
                  'sorting':'ReleaseDate',
                  'popFilter':'All',
                  'deviceFilter':'All',
                  'page':pageNumber,
                  'appsPerPage':'10'}
        request = requests.post(url, json=params)
        if request.status_code != 200:
            return
        requestDict = request.json()
        json_obj = json.loads(requestDict.get('d'))
        appIdList = json_obj.get("ResultSet")
        return appIdList

    def downloadAppUrl(self,appIdList):
        if appIdList is None:
            return
        appUrls=set()
        url='http://www.appzapp.us/Service/listings.asmx/GetAppDetail'
        for appId in appIdList:
            params={'id':str(appId)}
            try:
                request = requests.post(url, json=params)
            except:
                continue
            if request.status_code != 200:
                continue
            requestDict = json.loads(request.json().get('d'))
            appUrlTitle = requestDict.get('UrlTitle')
            appUrl = 'http://www.appzapp.us/App/'+appUrlTitle + '-' + str(appId) + '.html'
            appUrls.add(appUrl)
        return appUrls




