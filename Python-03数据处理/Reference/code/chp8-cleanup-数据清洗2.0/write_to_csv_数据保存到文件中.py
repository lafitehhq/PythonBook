# -*- coding: utf-8 -*-

"""
Description:
    数据保存到文件中

"""

from csv import writer
from get_zipped_data import get_zipped_data

def write_file(zipped_data, file_name):
    with open(file_name, 'wb') as new_csv_file:  # with...as 的作用是将第一个函数的输出赋值给第二个变量名。本行代码将新文件open(file_name, 'wb') 赋值给变量new_csv_file。'wb'的意思是以二进制模式写入。
        wrtr = writer(new_csv_file)  # 初始化CSV writer对象，传入一个打开的文件，然后将writer 对象赋值给wrtr 变量。
        titles = [row[0][1] for row in zipped_data[0]]  # writer 对象需要数据列表来逐行写入，本行创建的是标题行的标题列表。长标题是元组第一部分的第二个元素，所以对应的代码是row[0][1]。
        wrtr.writerow(titles)  # 用到了writer 对象的writerow方法，将一个可迭代对象转换成一行逗号分隔的数据。本行代码写入的是标题行。
        for row in zipped_data:
            answers = [resp[1] for resp in row]  # 利用列表生成式提取出所有回答（元组的第二个元素）。
            wrtr.writerow(answers)

write_file(get_zipped_data(), 'cleaned_unicef_data.csv')  # 利用列表生成式创建的所有列表或回答写入CSV数据文件
print 'Finish!'