import urllib2
import json
import urllib
import Po.Data
import requests

from View import Cookie

data=Po.Data.data()
cookieJar=Cookie.cookieJar()
values={'username':data.getUsername(),'password':data.getPassword()}
requestData=urllib.urlencode(values)
userAgent=data.getUseraAgent()
headers={
    "Content-type":"application/json; charset=utf-8",
    'User-Agent':userAgent,
         'Referer':data.getReferer()
}

if __name__ == "__main__":
    url = 'http://www.appzapp.us/Service/listings.asmx/GetGenreListing'
    params = {'genre': 6000,
              'priceFilter': 'All',
              'sorting': 'ReleaseDate',
              'popFilter': 'All',
              'deviceFilter': 'All',
              'page': 1,
              'appsPerPage': '10'}
    request = requests.post(url, json=params)
    requestDict = request.json()
    json_obj = json.loads(requestDict.get('d'))
    appIdList = json_obj.get("ResultSet")
    print appIdList

    appUrls = set()
    url = 'http://www.appzapp.us/Service/listings.asmx/GetAppDetail'
    for appId in appIdList:
        params = {'id': str(appId)}
        request = requests.post(url, json=params)
        if request.status_code != 200:
            continue
        requestDict = json.loads(request.json().get('d'))
        appUrlTitle = requestDict.get('UrlTitle')
        appUrl = 'http://www.appzapp.us/App/' + appUrlTitle + '-' + str(appId) + '.html'
        print appUrl


