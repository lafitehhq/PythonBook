# .next_siblings：用于处理兄弟标签

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 使用BeautifulSoup获取网页源代码
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, 'lxml')

# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
for sibling_1 in bsObj.find("table", id='giftList').tr.next_siblings:  # 等效于上面的写法
    print(sibling_1)


