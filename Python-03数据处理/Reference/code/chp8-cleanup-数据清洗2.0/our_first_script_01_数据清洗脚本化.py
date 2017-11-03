# -*- coding: utf-8 -*-

"""
Description:
    数据清洗脚本化1.0
    思路：
        • 从UNICEF 数据文件中导入数据。
        • 找到数据行对应的标题。
        • 将我们可以读懂的标题与内置缩写标题正确匹配。
        • 解析数据，检查是否有重复值。
        • 解析数据，检查数据是否有缺失。
        • 将同一家庭的多行数据合并。
        • 保存数据。
拓展：

"""

from csv import reader
import dataset

data_rdr = reader(open('..\..\data\unicef\mn.csv'.decode('utf8'), 'rb'))
header_rdr = reader(open('..\..\data\unicef\mn_headers_updated.csv'.decode('utf8'), 'rb'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]

all_short_headers = [h[0] for h in header_rows]

skip_index = []
final_header_rows = []

for header in data_rows[0]:
    if header not in all_short_headers:
        print header
        index = data_rows[0].index(header)
        if index not in skip_index:
            skip_index.append(index)
    else:
        for head in header_rows:
            if head[0] == header:
                final_header_rows.append(head)
                break

new_data = []

for row in data_rows[1:]:
    new_row = []
    for i, d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
    new_data.append(new_row)

zipped_data = []

for drow in new_data:
    zipped_data.append(zip(final_header_rows, drow))

# 检查数据是否有缺失

for x in zipped_data[0]:
    if not x[1]:
        print x

# 检查是否有重复值

set_of_keys = set([
    '%s-%s-%s' % (x[0][1], x[1][1], x[2][1]) for x in zipped_data])

uniques = [x for x in zipped_data if not
           set_of_keys.remove('%s-%s-%s' %
                              (x[0][1], x[1][1], x[2][1]))]

print len(set_of_keys)

# 保存到数据库

db = dataset.connect('sqlite:///C:\sqlite\data_wrangling.db')

table = db['unicef_survey']

for row_num, data in enumerate(zipped_data):
    for question, answer in data:
        data_dict = {
            'question': question[1],
            'question_code': question[0],
            'answer': answer,
            'response_number': row_num,
            'survey': 'mn',
        }

    table.insert(data_dict)
