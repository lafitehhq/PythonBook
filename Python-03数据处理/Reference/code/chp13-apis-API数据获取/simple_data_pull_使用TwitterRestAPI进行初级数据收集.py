# -*- coding: utf-8 -*-

"""
Description：

拓展：

"""
import oauth2

API_KEY = '5Hqg6JTZ0cC89hUThySd5yZcL'
API_SECRET = 'Ncp1oi5tUPbZF19Vdp8Jp8pNHBBfPdXGFtXqoKd6Cqn87xRj0c'
TOKEN_KEY = '3272304896-ZTGUZZ6QsYKtZqXAVMLaJzR8qjrPW22iiu9ko4w'
TOKEN_SECRET = 'nsNY13aPGWdm2QcgOl0qwqs5bwLBZ1iUVS2OE34QsuR4C'


def oauth_req(url, key, secret, http_method="GET", post_body="",
              http_headers=None):
    consumer = oauth2.Consumer(key=API_KEY, secret=API_SECRET)  # 创建一个 oauth2 对象的消费者。消费者是 key 的所有者。这行代码给消费者提供 key，这样消费者可以顺利地通过 API 识别。
    token = oauth2.Token(key=key, secret=secret)  # 将 token 赋值给 oauth2 对象。
    client = oauth2.Client(consumer, token)  # 创建客户端，包含消费者和 token。
    resp, content = client.request(url, method=http_method,
                                   body=post_body, headers=http_headers)  # 使用函数参数 url，通过 OAuth2 客户端执行请求
    return content   # 返回从连接接收到的内容。


# 上面步骤有了一个函数，允许我们连接到 Twitter API。
# 然而，我们需要定义 URL，并且调用函数。搜索 API 文档（https://dev.twitter.com/rest/public/search）告诉我们更多有关想要使用的请求的信息。
# 使用 Web 接口，可以看到，如果搜索 #childlabor，最终得到的 URL 是：https://twitter.com/search?q=%23childlabor。文档建议重新格式化URL，所以最终的URL如下：https://api.twitter.com/1.1/search/tweets.json?q=%23childlabor。
url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23childlabor'  # 这个 URL 作为一个变量，并使用之前定义的变量调用函数：
data = oauth_req(url, TOKEN_KEY, TOKEN_SECRET)
print data  # 该看到数据打印成一个很长的 JSON 对象。你可能记得 JSON 对象看起来和 Python 字典类似，但是如果使用 print(type(data)) 重新运行脚本，你会发现内容是一个字符串。现在我们可以做以下两件事情中的一件：转化数据为一个字典并开始解析它，或者保存字符串到一个文件，之后再解析。为了继续在脚本中解析数据，在脚本顶部添加 import json。之后，在尾部，使用 json 加载字符串，并且输出它。

with open("../../data/chp13/hashchildlabor.json", "w") as data_file:  # 变量 data 现在会返回一个 Python 字典。如果你想要将数据写入一个文件并且在之后解析它
    data_file.write(data)
