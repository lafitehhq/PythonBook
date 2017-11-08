# -*- coding: utf-8 -*-

"""
Description：

拓展：
①：find 和 cssselect 的操作方式有很大的不同。find 利用 DOM 来遍历元素，并基于
祖先和家族关系找到它们，而 cssselect 方法利用 CSS 选择器来寻找页面中所有可能的匹
配，或者元素的后继，非常类似于 jQuery。根据需求的不同，find或cssselect可能更加有用。如果页面的 CSS类、ID
和其他标识符组织得良好，cssselect是一个非常棒的选择。但是如果页面没
有组织或不使用这些标识符，遍历DOM可以帮助你通过家族关系确定内容。

"""

from lxml import html
from lxml import etree
import sys

page = html.parse('http://www.enoughproject.org/take_action')  # 使用 lxml 的解析方法，它可以从一个文件名、一个打开的缓冲区或一个合法的URL解析。它返回一个 etree 对象。
print page
root = page.getroot()  # 因为 etree 对象的方法和属性比 HTML 元素对象少很多，所以这行代码访问根（页面和 HTML 的顶部）元素。根包含所有可能的能够访问的主干（孩子）和细枝（后代）。从根可以向下解析每一个链接或者段落，并且可以返回整个页面的head和body标签。
print root
ta_divs = root.cssselect('div.views-row')  # 使用根元素，这行代码找到所有的类名称为 views-row 的 div。它使用 cssselect 方法和一个CSS选择器字符串，返回一个匹配元素的列表。
print ta_divs

all_data = []

for ta in ta_divs:
    data_dict = {}
    title = ta.cssselect('h2')[0]  # 为了抓取标题，使用 cssselect 方法找到 h2 标签。这行代码选择了列表中的第一个元素。cssselect返回一个所有匹配项的列表，但是我们只想要第一个匹配的元素。
    data_dict['title'] = title.text_content()  # 同 Beautiful Soup 的 get_text 方法类似，text_content 为 lxml HTML 元素对象返回标签（和任何子标签）内的文本。
    data_dict['link'] = title.find('a').get('href')  # 使用链式方法来从 title 元素中获得锚标签，并且拉取锚标签中的 href 属性。这只返回这一属性的值，类似于Beautiful Soup的 get方法。
    data_dict['about'] = [p.text_content() for p in ta.cssselect('p')]  # 使用列表生成式来从 Take Action div 中的每一个段落中拉取文本，组成完整的文本。
    all_data.append(data_dict)

print all_data

print root.find('div')  # 在根元素上使用 find 方法来找到 div，这返回空。从浏览器的检视来看，我们知道页面充满了divs

print root.find('head')

print root.find('head').findall('script')  # 使用find 方法查看头部标签，使用findall方法在头部定位脚本元素。

print root.cssselect('div')  #  使用cssselect 取代find 正确地定位文档中所有的divs，它们作为一个大的列表返回。

print root.cssselect('head script')  # 使用 cssselect，通过嵌套 CSS 选择器在头部定位脚本标签。使用 head script 返回与从根对象链式调用find 命令相同的列表。



# from lxml import etree
# import sys
#
# html = '''
# <html>
# 　　<head>
# 　　　　<meta name="content-type" content="text/html; charset=utf-8" />
# 　　　　<title>友情链接查询 - 站长工具</title>
# 　　　　<!-- uRj0Ak8VLEPhjWhg3m9z4EjXJwc -->
# 　　　　<meta name="Keywords" content="友情链接查询" />
# 　　　　<meta name="Description" content="友情链接查询" />
#
# 　　</head>
# 　　<body>
# 　　　　<h1 class="heading">Top News</h1>
# 　　　　<p style="font-size: 200%">World News only on this page</p>
# 　　　　Ah, and here's some more text, by the way.
# 　　　　<p>... and this is a parsed fragment ...</p>
#
# 　　　　<a href="http://www.cydf.org.cn/" rel="nofollow" target="_blank">青少年发展基金会</a>
# 　　　　<a href="http://www.4399.com/flash/32979.htm" target="_blank">洛克王国</a>
# 　　　　<a href="http://www.4399.com/flash/35538.htm" target="_blank">奥拉星</a>
# 　　　　<a href="http://game.3533.com/game/" target="_blank">手机游戏</a>
# 　　　　<a href="http://game.3533.com/tupian/" target="_blank">手机壁纸</a>
# 　　　　<a href="http://www.4399.com/" target="_blank">4399小游戏</a>
# 　　　　<a href="http://www.91wan.com/" target="_blank">91wan游戏</a>
# 	   <div class="news">
# 	    1. <b>无流量站点清理公告</b>  2013-02-22<br />
# 	    取不到的内容11
# 	    </div>
# 	    <div class="news">
# 	    2. <strong>无流量站点清理公告</strong>  2013-02-22<br />取不到的内容22
# 	    </div>
# 	    <div class="news"> 3. <span>无流量站点清理公告</span>  2013-02-22<br />取不到的内容33
# 	    </div>
# 	    <div class="news"> 4. <u>无流量站点清理公告</u>  2013-02-22<br />取不到的内容44
# 	    </div>
# 	　　</body>
# </html>
# '''
#
# page = etree.HTML(html.decode('utf-8'))#先确保html经过了utf-8解码，即code = html.decode('utf-8', 'ignore')，否则会出现解析出错情况。因为中文被编码成utf-8之后变成 '/u2541'　之类的形式，lxml一遇到　“/”就会认为其标签结束。
# hrefs = page.xpath("//a")#它会找到整个html代码里的所有a标签，如果想精确地获取，可以采用下面获取p标签的方法
# for href in hrefs:
# 	print href.get('href')
# 	print href.text.encode("utf-8")
# 	print '*'*20+'华丽的星号分界线'+'*'*20
#
# ps = page.xpath("/html/body/p[@style='font-size: 200%']")#精确获取p标签，如果使用xpath('//p')将会找到整个html代码里的所有p标签
# #等价ps = page.xpath("//p[@style='font-size: 200%']")#相对路径
# #等价ps = page.xpath("//p[text()='World News only on this page']")#标签里面没有属性时，为了精确获取某个标签，可以使用text()，position()等方法来过滤
# for p in ps:
# 	print p.values()
# 	print p.text.encode('utf8')#获取p标签下的文本内容
#
# print '-'*40+"华丽的分界线"+'-'*40
#
# hard_get = page.xpath("//br")
# for hg in hard_get:
# 	print '---'+hg.tail.encode('utf8').strip()+'---'#使用lxml.etree._Element的tail属性来获取br标签后面紧跟的文本内容（仅仅使用xpath是很难获取这个内容的）
#
# print '-'*40+"华丽的分界线"+'-'*40
#
# html1 = """
# <html><head><title>为什么len(y) <= 1</title><script>var y = 1</script></head>sample.<html>
# """
# #lxml.etree.HTML可以处理内容中含有特殊字符的情况，如上边title标签的文本内容中含有"<"。
# page1 = etree.HTML(html1.decode('utf8'))
# title = page1.xpath("//title")[0].text
# print 'title:%s'%title.encode('utf-8')
#
# print '-'*40+"华丽的分界线"+'-'*40
#
# #bs4的BeautifulSoup解析器也可以处理内容中含有特殊字符的情况，如上边title标签的文本内容中含有"<"。
# from bs4 import BeautifulSoup
#
# root = BeautifulSoup(''.join(html1),'lxml')
# print "Title is : " + root.head.title.string.encode('utf8')
#
# print '-'*40+"华丽的分界线"+'-'*40
#
# from lxml.html import clean
# #如果script与style标签之间的内容影响解析页面，或者页面很不规则，可以使用lxml.html.clean模块。模块 lxml.html.clean 提供 一个Cleaner 类来清理 HTML 页。它支持删除嵌入或脚本内容、 特殊标记、 CSS 样式注释或者更多。
# #注意,page_structure,safe_attrs_only为False时保证页面的完整性，否则，这个Cleaner会把你的html结构与标签里的属性都给清理了。使用Cleaner类要十分小心，小心擦枪走火。
# cleaner = clean.Cleaner(style=True,scripts=True,page_structure=False,safe_attrs_only=False)
# print '原始字符串:\n%s' % html1.strip()
# print 'clean_up之后的字符串:\n%s' %cleaner.clean_html(html1.decode('utf8')).encode('utf8').strip()