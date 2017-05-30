# coding=utf-8
import Html_Downloader

from Service import Html_Parser
from Service import Url_Manager
from Po import Data
from Dao import Html_Outputer

data=Data.data()
class SpiderMain(object):
    def __init__(self):
        self.htmlParser=Html_Parser.HtmlParser()
        self.urlManager=Url_Manager.UrlManager()
        self.htmlOutputer=Html_Outputer.HtmlOutputer()
        self.htmlDownloader=Html_Downloader.HtmlDownloader()

    def craw(self,url,typeNumber):
        count=0
        typeDict=data.getTypeDict()
        print 'Current type number: '+str(typeNumber)
        type=typeDict.get(str(typeNumber))
        print 'Current type: '+type
        self.urlManager.addNewUrl(url)
        while self.urlManager.hasNewUrl():
            try:
                newUrl=self.urlManager.getNewUrl()
                htmlContent=self.htmlDownloader.download(newUrl)
                newUrls,newData=self.htmlParser.parse(newUrl,htmlContent)
                self.urlManager.addNewUrls(newUrls)
                self.htmlOutputer.collectData(newData)
                self.htmlOutputer.outputHtml(type)
                print '1 piece of information has been crawed'
            except:
                return


