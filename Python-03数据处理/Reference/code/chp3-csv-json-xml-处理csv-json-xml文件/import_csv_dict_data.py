# -*-coding:utf8-*-

"""
Description：
利用csv库DictReader查看csv文件数据
"""
import csv

csvfile = open('../../data/chp3/data-text.csv', 'rb')
reader = csv.DictReader(csvfile)  # csv.DictReader()返回的是一个列表

for row in reader:
    print row
