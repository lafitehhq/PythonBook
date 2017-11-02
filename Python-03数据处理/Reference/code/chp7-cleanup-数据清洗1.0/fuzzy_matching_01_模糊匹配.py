# -*- coding: utf-8 -*-

""" 
@File: fuzzy_matching_01_模糊匹配.py 
@Version:
@Description:

拓展：
①：python-Levenshtein模块的安装：https://zhidao.baidu.com/question/1798588994814415347.html
"""

from fuzzywuzzy import fuzz

my_records = [{'favorite_book': 'Grapes of Wrath',
               'favorite_movie': 'Free Willie',
               'favorite_show': 'Two Broke Girls',
               },
              {'favorite_book': 'The Grapes of Wrath',
               'favorite_movie': 'Free Willy',
               'favorite_show': '2 Broke Girls',
               }]

print fuzz.ratio(my_records[0].get('favorite_book'),  # fuzz 模块的 ratio 函数，接受两个字符串作比较。返回的是两个字符串序列的相似程度（一个介于 1 和 100之间的值）。
                 my_records[1].get('favorite_book'))

print fuzz.ratio(my_records[0].get('favorite_movie'),
                 my_records[1].get('favorite_movie'))

print fuzz.ratio(my_records[0].get('favorite_show'),
                 my_records[1].get('favorite_show'))

print '---'*20

print fuzz.partial_ratio(my_records[0].get('favorite_book'),  # 是 fuzz 模块的 partial_ratio 函数，接受两个字符串作比较。返回的是匹配程度最高的子字符串序列的相似程度（一个介于1和100之间的值）。
                         my_records[1].get('favorite_book'))

print fuzz.partial_ratio(my_records[0].get('favorite_movie'),
                         my_records[1].get('favorite_movie'))

print fuzz.partial_ratio(my_records[0].get('favorite_show'),
                         my_records[1].get('favorite_show'))

