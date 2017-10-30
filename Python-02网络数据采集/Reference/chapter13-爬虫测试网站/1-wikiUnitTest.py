# 使用unittest模块进行单元测试2.0

from urllib.request import urlopen
from urllib.parse import unquote
import random
import re
from bs4 import BeautifulSoup
import unittest

class TestWikipedia(unittest.TestCase):
    
    bsObj = None
    url = None
 

    def test_PageProperties(self):
        global bsObj
        global url

        url = "http://en.wikipedia.org/wiki/Monty_Python"
        #Test the first 100 pages we encounter
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url), 'lxml')
            titles = self.titleMatchesURL()
            self.assertEquals(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print("Done!")

    # 是测试页面的标题是否为“Monty Python”
    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/")+6):]
        urlTitle = urlTitle.replace("_", " ")
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    # 测试页面是否有一个 div 节点id 属性是"mw-content-text"。
    def contentExists(self):
        global bsObj
        content = bsObj.find("div",{"id":"mw-content-text"})
        if content is not None:
            return True
        return False

    # 返回随机链接
    def getNextLink(self):
        global bsObj
        links = bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
        link = links[random.randint(0, len(links)-1)].attrs['href']
        print("Next link is: "+link)
        return "http://en.wikipedia.org"+link

if __name__ == '__main__':
    unittest.main()
