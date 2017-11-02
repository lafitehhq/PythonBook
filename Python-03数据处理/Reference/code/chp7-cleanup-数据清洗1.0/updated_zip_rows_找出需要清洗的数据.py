#-*-coding:utf-8_-*-
"""
# Todo
Description:
    合并问题与答案2.0
"""

from csv import reader

data_rdr = reader(open('../../data/unicef/mn.csv', 'rb'))
header_rdr = reader(open('../../data/unicef/mn_headers_updated.csv', 'rb'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]  # 使用列表生成式快速删除不匹配的标题(如果标题行第一个元素（标题缩写）包含在数据行的标题中，那么将该标题行添加到新列表中。),还在列表生成式中使用了 if 语句。

print len(header_rows)
print '--'*20

all_short_headers = [h[0] for h in header_rows]
skip_index = []  # 创建新列表，用来保存我们不希望保存的数据行的索引编号
final_header_rows = []

# for header in data_rows[0]:
#     if header not in all_short_headers:
#         index = data_rows[0].index(header)  # 利用 Python 列表的 index 方法，返回不需要的索引编号，因为这些索引编号对应的标题没有包含在缩写列表中。下一行代码会将不匹配标题行的索引编号保存下来，这样我们就可以不采集这些数据
#         skip_index.append(index)
#     else:
#         for head in header_rows:
#             if head[0] == header:
#                 final_header_rows.append(head)
#                 break
#
# del all_short_headers
#
# new_data = []
#
# for row in data_rows[1:]:  # 对保存调查数据的列表做切片，只选取其中的数据行（除了第一行外的所有行），然后对其进行遍历。
#     new_row = []
#     for i, d in enumerate(row):  # 利用 enumerate 函数找出不需要保存的那些数据行。这个函数接受一个可迭代对象（本例中是数据行列表），返回每一个元素的索引编号和值。该函数将返回的第一个值（索引编号）赋值给i，将数据值赋值给d。
#         if i not in skip_index:  # 检查并确保索引编号不在不希望保存的列表中
#             new_row.append(d)
#         new_data.append(new_row)  # 检查完数据行中的每一项（或每一“列”）之后，将新的数据条目添加到 new_data 列表中。

# zipped_data = []
#
# for drow in new_data:
#     zipped_data.append(zip(header_rows, drow))  # 将完全匹配的标题和数据合并在一起，并添加到新数组zipped_data
#     print zipped_data
# print '--'*20

data_headers = []

for i, header in enumerate(data_rows[0]):  # 遍历数据列表中的所有标题。
    if i not in skip_index:  # 利用if...not in... 语句，只有当索引编号不包含在skip_index 中时才会返回True。
        data_headers.append(header)

header_match = zip(data_headers, all_short_headers)  # 将两个标题列表合并在一起

print header_match
