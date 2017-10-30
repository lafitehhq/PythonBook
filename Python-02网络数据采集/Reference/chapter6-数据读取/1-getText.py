# 使用request模块中的urlopen函数对txt格式文本进行UTF-8编码再提取

from urllib.request import urlopen

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")

# print(textPage.read())  # 没有对内容进行编码再提取
print(str(textPage.read(), 'utf-8'))