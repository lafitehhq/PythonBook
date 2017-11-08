# -*- coding: utf-8 -*-

"""
Description:
    
拓展：
①：根据请求的复杂度，还可以使用 requests 库（http://docs.python-requests.org/en/latest/）。
requests 使用 urllib 和 urllib2，让复杂的请求更容易格式化和发送。如果你需要格式
化一个复杂的文件 post请求(http://docs.python-requests.org/en/latest/user/quickstart/#morecomplicated-post-requests)
或查看session(http://docs.python-requests.org/en/latest/user/quickstart/#cookies)中还存留了什么 cookie，
或者检查响应状态码(http://docs.python-requests.org/en/latest/user/quickstart/#response-status-codes)
②：在检查网络（或时间线）标签时，有些时候会发现一些使用特殊 HTTP 头
（http://en.wikipedia.org/wiki/List_of_HTTP_header_ﬁelds）、cookies 或其他认
证方法的页面。你可以使用 urllib2、urllib 或 requests 库，同请求一起发
送这些特殊字段。


"""
import urllib
import urllib2

google = urllib2.urlopen('http://baidu.com')  # 使用urlopen 方法来开始请求返回一个缓冲区可以读取网页的内容。
google = google.read()  # 读取整个页面的内容到google 变量中
print google[:200]  # 打印前 200 个字符，这样可以看到页面的开端

url = 'http://baidu.com/s?'
url_with_query = url + urllib.quote_plus('python web scraping')  # 使用 quote_plus 方法来用加号转义字符串。这在处理网站的查询字符串时很有用——我们想要使用Google 搜索网页结果，同时我们知道Google 希望得到一个在单词之间使用加号连接的查询字符串。

web_search = urllib2.urlopen(url_with_query)
web_search = web_search.read()
print web_search[:200]
