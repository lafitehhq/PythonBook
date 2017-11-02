# -*- coding: utf-8 -*-

""" 
@File: fuzzy_matching_02_模糊匹配.py 
@Version:
@Description:
"""

from fuzzywuzzy import process

choices = ['Yes', 'No', 'Maybe', 'N/A']

print process.extract('ya', choices, limit=2)  # 利用 FuzzyWuzzy 的 extract 方法，将字符串与可能匹配的列表依次比较。函数返回的是 choices 列表中两个可能的匹配。

print process.extractOne('ya', choices)  # 利用 FuzzyWuzzy 的 extractOne 方法，返回 choices 列表中与我们的字符串对应的最佳匹配。

print process.extract('nope', choices, limit=2)

print process.extractOne('nope', choices)