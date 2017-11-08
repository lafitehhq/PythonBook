# -*- coding: utf-8 -*-

"""
拓展：
①：tweepy.API 对象可以接受不同的参数，这给了你请求数据时控制 tweepy 行为的能力。你
可以通过传递参数（像 retry_count=3, retry_delay=5）直接添加重试和延迟。另一个
有用的选项是 wait_on_rate_limit，这个选项会直到频率限制解除后再去做下一次请求。
tweepy 文档（http://docs.tweepy.org/en/latest/api.html）中有这些选项的细节和更多信息。
我们想要使用 tweepy.Cursor 创建一个和 Twitter API 的连接。然后将 API 方法（这里是
api.search，http://docs.tweepy.org/en/latest/api.html#API.search）和与其相关的参数传递给
指针（cursor）。

"""

import json
import tweepy
import dataset

API_KEY = '5Hqg6JTZ0cC89hUThySd5yZcL'
API_SECRET = 'Ncp1oi5tUPbZF19Vdp8Jp8pNHBBfPdXGFtXqoKd6Cqn87xRj0c'
TOKEN_KEY = '3272304896-ZTGUZZ6QsYKtZqXAVMLaJzR8qjrPW22iiu9ko4w'
TOKEN_SECRET = 'nsNY13aPGWdm2QcgOl0qwqs5bwLBZ1iUVS2OE34QsuR4C'

# 添加推文到简单的数据库
def store_tweet(item):
    db = dataset.connect('sqlite:///Users/lafitehhq/SQLlite/SqlLiteData/Userdata_wrangling.db')
    table = db['tweets']  # 创建或访问一个新表，名为 tweets。
    item_json = item._json.copy()  # 检查推文中是否含有字典对象。由于 SQLite 并不支持保存 Python 字典，我们需要将其转换为字符串。
    for k, v in item_json.items():
        if isinstance(v, dict):
            item_json[k] = str(v)
    table.insert(item_json)  # 插入合法的 JSON 对象。


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)  # 创建一个对象，通过 tweepy 来管理 API 认证。
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)  # 设置访问 token。


api = tweepy.API(auth)  # 将刚刚创建的认证对象传递给 tweepy.API：

query = '#childlabor'  # 创建 query 变量。
cursor = tweepy.Cursor(api.search, q=query, lang="en")  # 使用 query 创建 cursor，并且限制其只检索英语。

for page in cursor.pages():  # 对于每一个 cursor.pages() 返回的页面……
    tweets = []  # 创建一个空列表来保存推文。
    for item in page:  # 对于页面中的每一个对象（或推文）……
        tweets.append(item._json)  # 抽取 JSON 推文数据，保存到推文列表中。
with open('data/hashchildlabor.json', 'wb') as outfile:  # 打开一个名为 hashchildlabor.json 的文件，保存这些推文。
    json.dump(tweets, outfile)
