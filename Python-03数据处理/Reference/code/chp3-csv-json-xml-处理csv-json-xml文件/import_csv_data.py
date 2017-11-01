# -*-coding:utf8-*-

"""
Description：
利用csv库Reader查看csv文件数据

拓展：  
①：csv库：https://docs.python.org/2/library/csv.html
②：open()函数：https://docs.python.org/2/library/functions.html#open
"""

import csv

csvfile = open('../../data/chp3/data-text.csv', 'rb')  # open()是Python 的内置函数；'rb'以只读方式和二进制方式打开文件；'wb'，后者表示以二进制方式写入
reader = csv.reader(csvfile)  # 将csvfile传递给csv模块的reader函数，让csv模块将打开的文件当作CSV 来读取,返回的是一个列表,包含的是文件中的每一行数据

for row in reader:  # reader对象是一个保存数据行的 Python容器
    print row
