# -*- coding: utf-8 -*-

"""
Description:

拓展：
①：家族树通过 Beautiful Soup 库 page 类中的内置属性和方法导航。正如可以从头部和
导航栏示例中看到的那样，从页面中选择一个区域，并遍历孩子、后代或邻居是很容易
的。Beautiful Soup 的语法非常简单，并且将元素和它们的属性链式绑定到一起（像.head.
children）。
②：Beautiful Soup库的使用:(https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

"""
from bs4 import BeautifulSoup  # 直接从 beautifulsoup4库导入解析器。
import requests

page = requests.get('http://www.enoughproject.org/take_action')  # 使用requests 库来抓取页面上的内容，这行代码将响应（和它的内容）赋值给page变量。

bs = BeautifulSoup(page.content, 'lxml')  # 传递页面内容到 BeautifulSoup 类。可以使用 content 属性获取响应的源页面。



print bs.title
print '---'*20

print bs.find_all('a')   # 一旦解析了页面对象，可以使用它的属性和方法。这行代码让 Beautiful Soup 找到页面中所有的a 标签（或链接）。
print '---'*20

print bs.find_all('p')
print '---'*20

header_children = [c for c in  bs.header.children]  # 使用列表生成式创建一个页面中头部的所有子元素的列表。通过将Beautiful Soup 页面对象和 .head（调取页面的头部）以及 .children 联系在一起，可以查看所有包含在头部中的节点。如果需要的话，可以解析头部的元内容，包括页面描述。
print header_children
print '---'*20


# navigation_bar = bs.find_all(id="menu-get-involved")  # 如果使用开发者工具观察页面，会看到导航栏使用一个CSS选择器ID globalNavigation定义。这行代码使用页面对象的find方法，传递一个ID，并且定位导航栏。
# print navigation_bar
# print type(navigation_bar)

navigation_bar = bs.descendants
for d in navigation_bar:
    print d
print '---'*20

for s in d.previous_siblings:  # 到导航栏的最后一个后继，这行代码使用.previous_sibling来遍历导航元素的邻居。
    print s
print '---' * 20

ta_divs = bs.find_all("div", class_="views-row")  # 使用Beautiful Soup找到并返回类中包含字符串 views-row 的所有divs。
print len(ta_divs)  # 打印来检查数字是否是可以在网站上看到的故事行数，预示着正确地匹配了行数据。
print '---'*20

for ta in ta_divs:
    title = ta.h2  #  遍历这些行数据，并基于页面的研究获取想要的标签。标题位于一个h2 标签中，并且是行中唯一的 h2标签。链接是第一个锚标签。
    link = ta.a
    about = ta.find_all('p')  # 因为不确定在每行数据中有多少个段落标签，所以匹配所有的段落标签来得到文本。由于使用了.find_all方法，Beautiful Soup返回一个列表，而不是第一个匹配的元素。
    print title, link, about
print '---'*20

# 内容可能随着站点更新而改变，但是应该会看到一个h2 元素，之后是一个锚（a）元素，
# 然后是每个节点段落的列表。上面的的输出是混乱的，不仅因为正在使用一个print，还因为 Beautiful Soup 打印了完整的元素和它的内容。相对于完整的元素
# 现在数据和输出呈现了一个更加有组织的格式。在变量 all_data 中，保存了一个所有数据的列表。现在每一个数据输入都和匹配键保存在其字典中。
# 用一种整洁的方式，使用一些新的方法（get 和 get_text）从页面抓取了数据，并且数据现在存放在数据字典中。代码更加清晰和精确，可以通过添加辅助函数让它更加清晰
all_data = []

for ta in ta_divs:
    data_dict = {}
    data_dict['title'] = ta.h2.get_text()  # 使用get_text 方法抽取所有来自HTML 元素的字符串。这样会获得标题文本
    data_dict['link'] = ta.a.get('href')  # 为了得到一个元素的属性，使用 get 方法。当看到 <ahref="http://foo.com">Foo</a>，并想提取链接时，可以调用 .get("href") 来返回href 值（即，foo.com）。
    data_dict['about'] = [p.get_text() for p in ta.find_all('p')]  # 为了抽取段落文本，使用 get_text 方法，遍历 find_all 方法返回的段落。这行代码使用列表生成式来编译一个有着动作内容调用的字符串列表。
    all_data.append(data_dict)

print all_data
