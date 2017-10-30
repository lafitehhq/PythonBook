# 在html中通过CSS标签提取符合条件的所有元素

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 使用BeautifulSoup获取网页源代码
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

print('-'*50, '人物', '-'*50)
nameList = bsObj.findAll("span", {"class": "green"})  # 用BeautifulSoup模块的findAll函数抽取只包含在 <span class="green"></span> 标签里的文字
for name in nameList:
    print(name.get_text())  # .get_text() 会把这些超链接、段落和标签都清除掉，只剩下一串不带标签的文字

print('-'*50, '对话', '-'*50)
articleList = bsObj.findAll("span", {"class": "red"})
articleList = bsObj.findAll("span", {"class": "red"})
for article in articleList:
    print(article.get_text())