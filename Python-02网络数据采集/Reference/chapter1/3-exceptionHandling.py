# 完善使用BeautifulSoup模块获取域名的源代码解决
# 解决可能发生两种异常：
# • 服务器不存在
# • 网页在服务器上不存在（或者获取页面的时候出现错误）

# Todo:打印异常输出没解决

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):  # 创建一个getTitle函数用于返回网页的标题
    try:  # 检查服务器是否存在
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:  # 检查网页在服务器上是否存在（或者获取页面的时候是否出现错误）
        bsObj = BeautifulSoup(html.read(), 'lxml')
        title = bsObj.title
    except AttributeError as e:  # 调用的标签不存在，BeautifulSoup会返回None对象(html就是一个None对象)，再调用这个None对象的子标签(html.read()方法)会发生 AttributeError错误。
        return None

    return title

title = getTitle("http://www.pythonscraping.co/")
# title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")

if title == None:
    print("网页的标题元素找不到")
else:
    print(title)