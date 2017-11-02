#-*-coding:utf-8_-*-
"""
# Todo
Description:
    合并问题与答案3.0
"""

from csv import reader

data_rdr = reader(open('../../data/unicef/mn.csv', 'rb'))
header_rdr = reader(open('../../data/unicef/mn_headers_updated.csv', 'rb'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]

all_short_headers = [h[0] for h in header_rows]

skip_index = []
final_header_rows = []  # 创建新列表，包含顺序正确的最终标题行。

for header in data_rows[0]:
    if header not in all_short_headers:
        index = data_rows[0].index(header)
        skip_index.append(index)
    else:  # 利用else语句，只将匹配的列添加到列表中。
        for head in header_rows:  # 遍历header_rows，直到找到匹配为止。
            if head[0] == header:  # 检查标题缩写是否匹配。用 == 来检查匹配
                final_header_rows.append(head)
            break  # 找到匹配后，利用 break 退出 for head in header_rows 循环。这样速度更快且不会对结果造成影响。

    new_data = []

    for row in data_rows[1:]:
        new_row = []
        for i, d in enumerate(row):
            if i not in skip_index:
                new_row.append(d)
        new_data.append(new_row)

    zipped_data = []

    for drow in new_data:
        zipped_data.append(zip(final_header_rows, drow))  # 将新的final_header_rows 列表与标题行按顺序正确地合并在一起。

    # for x in zipped_data[0]:
    #     print 'Question: {}\nAnswer: {}'.format(x[0], x[1])  # format用{} 表示数据传入的位置，用\n 换行符来表示换行。
    # print '---'*20

    # for x in zipped_data[0]:
    #     print 'Question: {[1]}\nAnswer: {}'.format(x[0], x[1])
    # print '---'*20

    # example_dict = {
    #         'float_number': 1324.321325493,
    #         'very_large_integer': 43890923148390284,
    #         'percentage': .324,
    #     }
    #
    # string_to_print = "float: {float_number:.4f}\n"  # 用到了字典，利用键访问字典的值。用 : 来分隔键名和格式。.4f 的意思是，将数字转换成浮点数（f），保留四位小数（.4）。
    # string_to_print += "integer: {very_large_integer:,}\n"  # 数字格式不变（键名和冒号），插入逗号（,）作为千位分隔符。
    # string_to_print += "percentage: {percentage:.2%}"  # 数字格式不变（键名和冒号），插入百分号（%），小数部分保留两位有效数字（.2）。
    #
    # print string_to_print.format(**example_dict)  # 对长字符串调用 format 方法，并传入数据字典，用 ** 将字典拆包（unpack）。将Python 字典拆包，也就是将字典的键/ 值拆开，拆包后的键和值被传递给format 方法
    # print '---'*20

    for x in enumerate(zipped_data[0][:20]): # enumerate 函数来查看我们需要处理哪些行的数据。
        print x
