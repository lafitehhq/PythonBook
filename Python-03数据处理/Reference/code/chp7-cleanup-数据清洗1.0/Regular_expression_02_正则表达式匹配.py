# -*- coding: utf-8 -*-

""" 
@File: Regular_expression_02_正则表达式匹配.py 
@Version:
@Description:

拓展：
①：search 和 match 的区别
match从字符串的开头开始搜索，如果没有找到匹配，它会返回 None。与此相反，search 会继续向后搜索，直到找到匹配为止。只有到达字符串末尾还没有找到匹配时，search 才会返回None。
如果需要匹配以特定模式开头的字符串，用 match 比较好。如果只想在字符串中找到第一个匹配或任意匹配，最好选择search。
"""

import re

number = '\d+'  # 定义一个数字模式。加号表示贪婪匹配，所以它会尽可能匹配所有数字，直到遇到一个非数字字符为止。
capitalized_word = '[A-Z]\w+'  # 定义一个大写单词的匹配。这个模式使用方括号来定义更长模式的一部分。方括号的意思是希望第一个字母是大写字母。后面紧跟着的是一个连续的单词

sentence = 'I have 2 pets: Bear and Bunny.'

search_number = re.search(number, sentence)
print search_number.group()  # search 方法返回的是匹配对象

match_number = re.match(number, sentence)
# match_number.group()  # match 返回的是None，而不是匹配对象。

search_capital = re.search(capitalized_word, sentence)
print search_capital.group()

match_capital = re.match(capitalized_word, sentence)
# match_capital.group()