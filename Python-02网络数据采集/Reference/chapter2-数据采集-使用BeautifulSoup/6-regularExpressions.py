# re.compile()：使用变量代表正则表达式

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 使用BeautifulSoup获取网页源代码
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, 'lxml')

images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images: 
    print(image["src"])
