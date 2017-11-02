# -*- coding: utf-8 -*-

""" 
@File: Regular_expression_01_正则表达式匹配.py 
@Version:
@Description:
"""

import re

word = '\w+'  # findall 返回的是所有匹配组成的列表;定义一个普通字符串的基本模式。这个模式可以匹配包含字母和数字、但不包含空格和标点的字符串。这个模式会一直匹配，直到无法匹配为止（+ 表示贪婪匹配！）。
sentence = 'Here is my sentence.'

print re.findall(word, sentence)  # re 模块的 findall 方法可以找出这个模式在字符串中的所有匹配。成功匹配了句子中的每一个单词，但没有匹配句号。在这个例子中我们用的模式是 \w，所以不会匹配标点和空格。

search_result = re.search(word, sentence)  # search方法可以在整个字符串中搜索匹配。发现匹配后，则返回匹配对象。
print search_result.group()  # 匹配对象的 group方法会返回匹配的字符串。

match_result = re.match(word, sentence)  # match方法只从字符串开头开始搜索。它的工作原理与search 不同。
print match_result.group()