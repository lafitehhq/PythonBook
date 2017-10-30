# 使用BeautifulSoup模块对txt格式文本进行UTF-8编码再提取
# 解决：Python把文本读成ASCII编码格式，而浏览器把文本读成 ISO-8859-1 编码格式


from urllib.request import urlopen
from bs4 import BeautifulSoup

# 使用BeautifulSoup获取网页源代码
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "lxml")

content = bsObj.find("div", {"id": "mw-content-text"}).get_text()  # bsObj.find():寻找第一个符合条件的div；.get_text():获取当前标签的内容
content = bytes(content, "UTF-8")  # 对标签内容用utf-8格式转换成bytes
content = content.decode("UTF-8")  # 对bytes内容用utf-8格式编码
print(content)