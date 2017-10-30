# 使用request模块获取域名的源代码

from urllib.request import urlopen  #查找request 模块（在 urllib 库里面），只导入urlopen函数

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
print(html.read())