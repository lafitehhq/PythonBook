# -*- coding: utf-8 -*-

import requests

google = requests.get('http://baidu.com')  # 调用requests 库的get 方法发送一个GET请求到 URL地址

print google.status_code  # 调用 status_code 属性来确保得到了 200 响应（正确地完成请求）。如果没有得到 200，可以以不同方式执行脚本逻辑。
print '---'*20

print google.content[:200]
print '---'*20

print google.headers  # # 检查响应的headers属性来看Google返回了什么头部。可以看到headers属性是一个字典
print '---'*20

print google.cookies.items()  # 使用 cookies 属性读取 Google 在响应中发送的 cookie，并且在返回的字典上调用 items方法来展示键/值对。
print '---'*20