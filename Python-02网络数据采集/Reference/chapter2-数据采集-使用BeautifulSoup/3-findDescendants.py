# .children：用于处理子标签和其他后代标签

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 使用BeautifulSoup获取网页源代码
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, 'lxml')

# for child in bsObj.find("table", {"id": "giftList"}).children:  # 打印giftList表格中所有产品的数据行
for child in bsObj.find("table", id='giftList').children:  # 等效于上面的写法
    print(child)

