# lambda函数/匿名函数的使用：https://www.zhihu.com/question/20125256

# Todo

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page2.html")
bsObj = BeautifulSoup(html, 'lxml')

tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)  # 获取有两个属性的标签
for tag in tags:
	print(tag)