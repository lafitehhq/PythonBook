# -*- coding: utf-8 -*-

"""
Description:
    将清洗过的数据保存到 SQLite 数据库
"""

import dataset
from get_zipped_data import get_zipped_data

db = dataset.connect('sqlite:///C:\sqlite\data_wrangling.db')  # 访问本地数据库。如果将文件保存到其他目录，一定要修改文件路径，将其修改为数据库文件相对于当前目录的位置

table = db['unicef_survey']  # 创建一个新表：unicef_data。很多 UNICEF 调查都有相同的规律，所以我们这个数据库名是没有歧义、可复用的

for row_num, data in enumerate(get_zipped_data()):  # 希望保存所在的行编号，这样每个回答都有一个编号。本行代码用到了enumerate函数，这样在数据库中可以找到（每一行 / 每一个回答的）每一条数据（它们的共用一个行编号）。
    for question, answer in data:  # 数据被分割成元组，标题列表是元组的第一个元素，问题回答是元组的第二个元素。本行代码利用for 循环解析其中包含的数据并进行存储。
        data_dict = {  # 每一个问题和回答在数据库中都有对应的条目，所以将每行（即每次采访）所有的回答合并在一起。本行代码创建一个字典，其中包含每次采访中每个回答的必要数据。
            'question': question[1],  # 标题列表中第二个元素是问题的详细说明。本行代码将其保存为 question，并将UNICEF问题代码保存为 question_code
            'question_code': question[0],
            'answer': answer,
            'response_number': row_num,  # 添加了enumerate 函数得到的rownum记录每一行回答（或每一次采访），
            'survey': 'mn',
        }
    table.insert(data_dict)  # 利用新表的insert 方法将新字典插入我们的数据库

print 'Finish!'
