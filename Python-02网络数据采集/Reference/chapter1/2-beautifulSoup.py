# 使用BeautifulSoup模块获取域名的源代码

from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen('http://www.fosota.com/')
html = urlopen('http://fund.eastmoney.com/allfund.html')
bsObj = BeautifulSoup(html.read(), 'lxml')

print('-'*30, '整个HTML文档', '-'*30)
print(bsObj.html)
# print('-'*30, '文档头', '-'*30)
# print(bsObj.head)
# print('-'*30, '文档标题', '-'*30)
# print(bsObj.title)
# print('-'*30, '文档样式', '-'*30)
# print(bsObj.style)
# print('-'*30, '网页显示内容', '-'*30)
# print(bsObj.body)
# print('-'*30, '网页显示的文字', '-'*30)
# print(bsObj.h1)
# print('-'*30, '网页显示的div', '-'*30)
# print(bsObj.div)
