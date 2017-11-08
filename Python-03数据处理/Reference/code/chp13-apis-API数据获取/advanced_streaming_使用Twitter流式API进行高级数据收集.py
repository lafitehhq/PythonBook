# -*- coding: utf-8 -*-

from tweepy.streaming import StreamListener  # 使用Twitter流式API进行高级数据收集
from tweepy import OAuthHandler, Stream  # 导入之前使用过的 OAuthHandler，以及 Stream，后者是真正处理 Twitter 的流信息的类。


API_KEY = '5Hqg6JTZ0cC89hUThySd5yZcL'
API_SECRET = 'Ncp1oi5tUPbZF19Vdp8Jp8pNHBBfPdXGFtXqoKd6Cqn87xRj0c'
TOKEN_KEY = '3272304896-ZTGUZZ6QsYKtZqXAVMLaJzR8qjrPW22iiu9ko4w'
TOKEN_SECRET = 'nsNY13aPGWdm2QcgOl0qwqs5bwLBZ1iUVS2OE34QsuR4C'


class Listener(StreamListener):  # 创建 StreamListener 的子类。

    def on_data(self, data):  # 定义 on_data 方法。
        print data  # 输出推文。
        return True  # 返回 True。StreamListener 有 on_data 方法，同样返回 True。因为创建了子类并重新定义了这个函数，所以必须在子类方法中重复返回这个值。

# 将 Listener 和 auth 传入到 Stream 中，开始使用搜索词过滤。
# 在这个案例中，我们查看 child labor（童工），因为它相对于 #childlabor 更加普遍。
auth = OAuthHandler(API_KEY, API_SECRET)  # 将 auth 和 Listener 作为参数传递，创建一个流。
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)  # 过滤流，只返回有 child 和 labor 存在的条目。

stream = Stream(auth, Listener())
stream.filter(track=['child labor'])
