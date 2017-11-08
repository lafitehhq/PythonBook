# -*- coding: utf-8 -*-

"""
Description:
拓展：
①：itersiblings 方法和 tag 属性帮助我们轻松地定位想要选择和解析的内容。在这个例子中，
我们没有使用任何 CSS 选择器。我们知道，代码不会因为添加一个新部分而损坏，只要页
面继续在头部和列表标签中保存内容。
②：为什么只想使用 HTML 元素构建一个解析器呢？不依赖于 CSS 类的优势是
什么？如果一个站点的开发者改变了它的设计或让它变得对移动端更友好，
那么很可能他会修改 CSS 和 JavaScript，而不是重新编写页面结构。如果使
用基本的页面结构驱动抓取器，它们可能会比那些使用CSS 的抓取器用得更
久，有效期更长。

"""

from lxml import html
import requests

resp = requests.get('http://www.emoji-cheat-sheet.com/')
page = html.document_fromstring(resp.content)   # 使用 requests 库拉取 HTML 文档的主体，之后使用 html 模块的 document_fromstring方法解析数据为一个HTML 元素。

body = page.find('body')
top_header = body.find('h2')  # 通过查看页面结构，可以看到这是一系列头部的匹配列表。这行代码定位第一个头部，这样我们可以使用家族关系来寻找其他有用的部分。

print top_header.text

headers_and_lists = [sib for sib in top_header.itersiblings()]  # 使用列表生成式和 itersiblings 方法（返回一个迭代器）来查看所有的邻居

print headers_and_lists

proper_headers_and_lists = [s for s in top_header.itersiblings() if
                            s.tag in ['ul', 'h2', 'h3']]  # 上一个 print 展示了初始的 itersibling 列表生成式返回了远超我们需求的数据，包括一些页面下方带有 div 和 script 元素的部分。使用页面检视，我们确定想要的标签只是ul、h2 和h3。这行代码使用列表生成式和一个 if 确保只返回目标内容。

print proper_headers_and_lists



