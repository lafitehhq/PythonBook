# -*- coding:utf-8 -*-
"""
------
Filename:   T04-testIpython4-逐行分析函数性能
date:   17/10/21
Description:    
    逐行分析函数性能：%prun和%run -p
------
"""

from numpy.random import randn

def add_and_sum(x, y):
    added = x + y
    summed = added.sum(axis=1)
    return summed

def call_function():
    x = randn(1000, 1000)
    y = randn(1000, 1000)
    return add_and_sum(x, y)




"""输入
%run T04-testIpython4-逐行分析函数性能.py
x = randn(3000,3000)
y = randn(3000,3000)
%prun add_and_sum(x, y)

"""