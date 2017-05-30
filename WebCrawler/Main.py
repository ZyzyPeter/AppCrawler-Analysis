# coding=utf-8
from View import SpiderMain
from View import Html_Downloader

htmlDownloader=Html_Downloader.HtmlDownloader()
if __name__ == "__main__":
    spiderMain=SpiderMain.SpiderMain()
    typeNumber=6000
    while typeNumber<=6020:
        if typeNumber==6019:
            continue
            #因为不知什么原因，恰好没有类型编码6019
        page = 1
        while page <= 100:
            appIdList=htmlDownloader.downloadPageUrl(page,typeNumber)
            appUrls=htmlDownloader.downloadAppUrl(appIdList)
            if appUrls is None:
                continue
            for url in appUrls:
                spiderMain.craw(url,typeNumber)
            print 'Page '+str(page)+' '+'has been crawed'

            '''if page==100:
                print '6018,1'
                exit()'''#用于防止爬虫中途停止而添加的手动调试部分

            page+=1
        typeNumber+=1




