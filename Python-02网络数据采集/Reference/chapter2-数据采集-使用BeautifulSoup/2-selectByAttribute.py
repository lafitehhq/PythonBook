# 在html中通过div标签提取符合条件的所有元素

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 使用BeautifulSoup获取网页源代码
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

allText = bsObj.findAll(id="text")  # 寻找所有标签包含（id="text"）关键字 的标签内容
print(allText[0].get_text())