# coding=utf-8
import urlparse

from bs4 import BeautifulSoup
from Util import Matcher

matcher = Matcher.Matcher()


class HtmlParser(object):
    def getNewUrls(self, newUrl, soup):
        newUrls = set()
        links = soup.find_all('a', href=matcher.getPattern('appLink'))
        for link in links:
            url = link['href']
            newFullUrl = urlparse.urljoin(newUrl, url)
            newUrls.add(newFullUrl)
        return newUrls

    def getNewData(self, newUrl, soup):
        newData = dict()
        newData['url'] = newUrl
        if matcher.getPattern('appLink').search(newUrl):
            try:
                # 如果正在爬取的页面是app页面
                '''
                <title id="ctl00_headTitle">AppZapp - 8bitWar: Apokalyps</title>
                '''
                nameNode = soup.find('title')
                newData['name'] = nameNode.get_text()
                '''
                <div id="PortalClicks"><b>7</b> Hits</div>
                '''
                hitNode = soup.find('div', id="PortalClicks").find('b')
                '''
                <div id="AppDetailLikes">Likes <b>0</b></div>
                '''
                likeNode = soup.find('div', id="AppDetailLikes").find('b')
                newData['hits'] = hitNode.get_text()
                newData['likes'] = likeNode.get_text()
                return newData
            except:
                return
        else:
            # 如果正在爬取的页面是目录页面
            return None

    def getNewAppUrls(self, soup):
        newUrls = set()
        links = soup.find_all('a', href=matcher.getPattern('appLink'))
        for link in links:
            url = link['href']
            newFullUrl = urlparse.urljoin('http://www.appzapp.us', url)
            newUrls.add(newFullUrl)
        return newUrls

    def parse(self, newUrl, htmlContent):
        if newUrl is None or htmlContent is None:
            return
        soup = BeautifulSoup(htmlContent, 'html.parser')
        newUrls = self.getNewUrls(newUrl, soup)
        newData = self.getNewData(newUrl, soup)
        return newUrls, newData

    def pageParse(self, driver):
        if driver is None:
            return
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        newAppUrls = self.getNewAppUrls(soup)
        return newAppUrls
