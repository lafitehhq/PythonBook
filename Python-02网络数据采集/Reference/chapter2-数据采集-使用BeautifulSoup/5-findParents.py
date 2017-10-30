# parent.previous_sibling:用于处理父标签

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 使用BeautifulSoup获取网页源代码
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, 'lxml')

# parent = bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()
parent = bsObj.find("img", src='../img/gifts/img1.jpg').parent.previous_sibling.get_text()
print(parent)
