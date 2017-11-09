# -*- coding: utf-8 -*-

from ghost import Ghost
from time import sleep

ghost = Ghost()  # 码调用 Ghost类的会话对象，实例化一个Ghost 对象来同页面交互。

with ghost.start(viewport_size=(1375, 769)) as session:
    page, extra_resources = session.open('http://python.org')  # Ghost 类的 open 方法返回两个对象，所以这行代码在两个独立的变量中捕获这些对象。第一个对象是用来同 HTML 元素交互的页面对象。第二个对象是页面加载的其他资源列表（你在网络标签中看到的列表）。

    print page
    print page.url
    print page.headers
    print page.http_status
    print page.content  # 页面对象有很多属性，比如头部、内容、链接和页面上的内容。这行代码打印页面的内容

    for r in extra_resources:
        print r.url  # 遍历页面的其他资源，并且打印它们，来看是否有用。有时，这些 URL 是API调用，可以利用它们简化数据的访问

    print page.content.contains('input')  # 测试页面上是否存在一个 input 标签（大多数的搜索框是简单的输入对象）。这会返回一个布尔值。
    result, resources = session.evaluate(
        'document.getElementsByTagName("input")')  #  使用一些简单的JavaScript 来找到页面上所有以“input”为标签名称的元素。
    print result.get('length')  # 打印来看响应中的JavaScript 数组的长度。


    result, resources = session.evaluate(
        'document.getElementsByTagName("input")[0].getAttribute("id");')  # 索引结果列表，获取id 属性。JavaScript直接给出了元素的CSS 属性，所以这是一个查看选择元素的相关 CSS的有用方式。
    print result

    result, resources = session.set_field_value("input", "scraping")
    print result

    try:
        page, resources = session.call("form", "submit", expect_loading=True)
    except Exception as e:
        print 'EXCEPTION: %s' % e

    result, resources = session.evaluate(
        'document.getElementsByTagName("input")[0].value = "scraping";')
    result, resources = session.evaluate(
        'document.forms[0].submit.click()')

    sleep(10)
    session.show()
    sleep(10)


