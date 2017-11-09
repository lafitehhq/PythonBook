# -*- coding: utf-8 -*-

from selenium import webdriver  # 导入来自Selenium的 webdriver 模块。这个模块用来调用任何已经安装的驱动器。
from time import sleep

# 获得一个页面加载完的浏览器对象（browser 变量）
browser = webdriver.Firefox()  #  通过使用 webdriver 模块的 Firefox 类初始化 Firefox 浏览器对象。这会在计算机上打开一个新的浏览器窗口。
browser.get('http://www.fairphone.com/we-are-fairphone/')  # 通过 get 方法和一个 URL 参数，访问想要抓取的 URL。打开的浏览器应该开始加载页面了
browser.maximize_window()  # 使用 maximize_browser 方法最大化打开的浏览器。这会帮助 Selenium“看到”更多的内容。


content = browser.find_element_by_css_selector('div.content')  # browser 对象有一个函数 find_element_by_css_selector，使用 CSS 选择器来选择HTML 对象。这行代码选择了第一个类名称为 content 的 div，这会返回第一个匹配的对象（一个 HTMLElement 对象）。

print content.text  # 打印第一个匹配对象的文本内容。

all_bubbles = browser.find_elements_by_css_selector('div.content')  # 码使用 find_elements_by_css_selector 方法，传递一个 CSS 选择器，找到所有匹配的对象。这个方法返回一个 HTMLElement 对象列表。

print len(all_bubbles)

for bubble in all_bubbles:  # 遍历列表，并且打印每一个对象的内容。
    print bubble.text

iframe = browser.find_element_by_xpath('//iframe')  # 使用find_element_by_xpath方法，返回第一个匹配iframe 标签的元素。

new_url = iframe.get_attribute('src')  # 得到src属性，这包含在 iframe中加载的页面的 URL。

browser.get(new_url)  # 在浏览器中加载 iframe的URL。

# 找到了如何加载想要的内容的方法现在看一下是否可以加载所有的内容气泡：

all_bubbles = browser.find_elements_by_css_selector('div.content')

for elem in all_bubbles:
    print elem.text

# browser.get('http://baidu.com')
#
# inputs = browser.find_elements_by_css_selector('form input')
# for i in inputs:
#     if i.is_displayed():
#         search_bar = i
#         break
#
# search_bar.send_keys('web scraping with python')
#
# search_button = browser.find_element_by_css_selector('form button')
# search_button.click()
#
# browser.implicitly_wait(10)
# results = browser.find_elements_by_css_selector('div h3 a')
#
# for r in results:
#     action = webdriver.ActionChains(browser)
#     action.move_to_element(r)
#     action.perform()
#     sleep(2)
#
# browser.quit()
