# -*- coding: utf-8 -*-

"""
Description:
    使用 XPath 语法重新编写 emoji 处理器，正确地存储每个部分中所有的emoji和头部信息
    

拓展：
①：虽然使用 CSS 选择器是一种找到页面上元素和内容的简单方式，也建议你学习和使用
XPath（https://en.wikipedia.org/wiki/XPath）。XPath 是一个标记模式选择器，组合了 CSS
选择器和遍历 DOM 的能力。理解 XPath 是学习网页抓取和网站结构的很好的方式。有了
XPath，你可以访问仅仅使用CSS选择器不容易阅读的内容。
XPath 可以用于几乎所有主要的网页抓取库，并且比其他大多数识别和同页
面内容交互的方法都快得多。事实上，大多数同页面交互的选择器方法都在
库内部转化为 XPath。
②：，通过 XPath 遍历 DOM 关系解析它，同时使用合适的属性或文本内容抓取出需要的内容。这段代码具有很好的扩展
性，如果页面的作者添加了更多的数据节，只要页面结构没有大幅度改变，解析器会继续
从页面拉取内容，并且我们会拿到不计其数的emoji表情！

"""

from lxml import html

page = html.parse('http://www.emoji-cheat-sheet.com/')
proper_headers = page.xpath('//h2|//h3')  # 寻找与emoji内容相关的头部信息。它使用XPath 抓取所有的 h2 和h3 元素
proper_lists = page.xpath('//ul')  # 每一个定位到的头部有一个ul 元素来匹配。这行代码在整个文档中收集所有的ul元素。

all_emoji = []

for header, list_cont in zip(proper_headers, proper_lists):  # 使用 zip 方法来打包头部和与之适合的列表，这返回一个元组列表。这行代码之后解包这些元组，使用一个 for 循环拉取每一个部分（头部与列表内容）到独立的变量中。
    section = header.text
    for li in list_cont.getchildren():  # 遍历 ul 元素的子元素（li 元素保存着emoji表情信息）。
        emoji_dict = {}
        spans = li.xpath('div/span')  # 通过页面检视，我们知道大多数的 li 元素有一个 div，其中包含两个 span 元素。这些 span 包括 emoji 表情的图片链接，以及用来唤起 emoji 表情的文字。这行代码使用XPath的 div/span 返回每个子div 元素下所有的span 元素。
        if len(spans):
            link = spans[0].get('data-src')  # 为了找到每个元素的链接，这行代码调用第一个 span 的 data-src 属性。如果 link 变量为None，代码会在我们的数据字典中设置emoji_link 属性为None。
            if link:
                emoji_dict['emoji_link'] = li.base_url + link  # 因为 data-src 保存着一个相对 URL，所以这行代码使用 base_url 属性来创建一个完整的绝对URL。
            else:
                emoji_dict['emoji_link'] = None
            emoji_dict['emoji_handle'] = spans[1].text_content()  # 抓取第二个span的文本。不同于链接的逻辑，我们不需要测试这是否存在，因为每一个emoji都拥有一个句柄
        else:
            emoji_dict['emoji_link'] = None
            emoji_dict['emoji_handle'] = li.xpath('div')[0].text_content()  # 对于包括 Basecamp 声效的页面，对于每一个列表对象，存在一个 div（你可以通过使用浏览器的开发者工具检视页面，轻松地找到它）。这行代码选择 div，并且抓取其中的文本内容。因为这行代码在 else 代码块中，所以我们知道这些只是声音文件，因为它们不使用 spans。
        emoji_dict['section'] = section
        all_emoji.append(emoji_dict)

print all_emoji
