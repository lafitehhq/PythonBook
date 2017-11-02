# -*- coding: utf-8 -*-

""" 
@File: Regular_expression_03_正则表达式匹配.py 
@Version:
@Description:
"""

import re

name_regex = '([A-Z]\w+) ([A-Z]\w+)'  # 用的是相同的大写单词语法，用了两次，分别放在括号里。括号的作用是分组。
names = "Barack Obama, Ronald Reagan, Nancy Drew"

name_match = re.match(name_regex, names)  # 在 match 方法里用的模式包含多个正则表达式组。如果找到匹配的话，将返回多个匹配组。
name_match.group()
name_match.groups()  # 对匹配结果调用groups 方法，返回找到的所有匹配组构成的列表

name_regex = '(?P<first_name>[A-Z]\w+) (?P<last_name>[A-Z]\w+)' # 为各组命名可以让代码清晰明确。在这个模式中，第一组叫 first_name，第二组叫last_name。

for name in re.finditer(name_regex, names):  # finditer 的作用与 findall 类似，但返回的是一个迭代器（iterator）。利用这个迭代器，可以逐个查看字符串中的匹配。
    print 'Meet {}!'.format(name.group('first_name'))  # 用字符串格式化的知识，打印出从每个匹配中仅提取名字（ﬁrst name）