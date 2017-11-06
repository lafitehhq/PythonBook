# -*- coding: utf-8 -*-

""" 

@Description:
"""
import dataset

db = dataset.connect('sqlite:///C:\sqlite\data_wrangling.db')

wm_count = db.query('select count(*) from unicef_survey where survey="wm"')  # 直接查询，可以快速查看 survey='wm'的行数。应该只包括将类型设为'wm' 后第二次运行的数据行

count_result = wm_count.next()  # 读取查询结果，利用查询响应的 next 方法提取出第一个结果。用的是 count，所以应该只得到一个结果。

print count_result