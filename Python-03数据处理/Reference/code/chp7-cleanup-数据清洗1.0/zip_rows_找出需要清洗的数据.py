#-*-coding:utf-8_-*-
"""
Description:
    合并问题与答案1.0
"""

from csv import reader  # 使用reader 类而不是 DictReader。reader 为每一行创建的是一个列表，而不是一个字典。由于要用的是 zip 方法，需要的是列表而不是字典，就可以将标题列表与数据列表合并在一起。

data_rdr = reader(open('../../data/unicef/mn.csv', 'rb'))
header_rdr = reader(open('../../data/unicef/mn_headers.csv', 'rb'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr]

print len(data_rows[0])  # 创建标题列表和数据列表，并查看长度是否相同。
print len(header_rows)   # 数据有 159 行,标题列表中有 210 个标题

print '---'*20


bad_rows = []
for h in header_rows:
    if h[0] not in data_rows[0]:  # 测试标题行的第一个元素（标题的缩写版本）是否包含在数据列表的第一行中（所有的标题缩写）。
        bad_rows.append(h)  # 将不匹配的标题行添加到新列表 bad_rows 中。下一步将利用这个列表来判断需要删除哪些行。

for h in bad_rows:
    header_rows.remove(h)  # 利用列表的 remove 方法从列表中删除指定的一行。

print len(header_rows)  # 数据列表中有159个值，标题列表中有150个值

all_short_headers = [h[0] for h in header_rows]  # 利用 Python 列表生成式采集每一个标题行的第一个元素，生成一个由所有标题缩写组成的列表。
for header in data_rows[0]:  # 遍历数据集中的所有标题，检查哪些没有包含在清洗后的标题列表中。
    if header not in all_short_headers:  # 挑出不包含在缩写列表中的标题
        print 'mismatch!', header  # print 语句打印出所有的不匹配项。如果需要将两个字符串打印在同一行中，只需要在中间加一个,，就可以用空格将两个字符串连接在一起
