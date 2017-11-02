#-*-coding:utf-8_-*-

"""
Description：
替换标题：将mn-headers.csv中标题与调查数据一一对应，这样就有了可读性较强的问题和答案

拓展：
①：Python 列表生成式的格式：
[func(x) for x in iter_x]
等效为
new_list = [] 
for x in iter_x: 
    new_list.append(func(x))
"""

from csv import DictReader

data_rdr = DictReader(open('../../data/unicef/mn.csv', 'rb'))
header_rdr = DictReader(open('../../data/unicef/mn_headers.csv', 'rb'))

data_rows = [d for d in data_rdr]  # 使用了列表生成式，将可迭代对象DictReader写入一个新列表，这样可以保存数据并重复使用
header_rows = [h for h in header_rdr]

# 2.1:使用列表的slice方法打印出数据的一个切片，显示新列表的前5个元素
print data_rows[:5]
print '---'*20

# 2.2
# for data_dict in data_rows:  # 遍历每一条数据记录,将用每一个字典的键与标题匹配
#     for dkey, dval in data_dict.items():  # 遍历每一行数据的键和值，这样就可以将所有键替换成可读性更强的标题标签（要查看数据字典里每一个键值对，我们用的是Python 字典的items 方法）。
#         for header_dict in header_rows:  # 遍历所有标题行，这样可以得到可读性更强的标签。这并不是最快的方法，但可以保证不会有遗漏。
#             for hkey, hval in header_dict.items():  # 如果数据列表的键（MWB3、MWB7、MWB4、MWB5…）和标题字典的值相同，那么打印'match!'表示二者相互匹配。
#                 if dkey == hval:
#                     print 'match!'
# print '---'*20

new_rows = []  # 创建一个新列表，里面包含的是清洗过的行数据

for data_dict in data_rows:  # 遍历每一条数据记录，将用每一个字典的键与标题匹配
    new_row = {}  # 为每一行创建一个新字典。
    for dkey, dval in data_dict.items():  # 遍历每一行数据的键和值，这样就可以将所有键替换成可读性更强的标题标签（要查看数据字典里每一个键值对，我们用的是Python 字典的items 方法）
        for header_dict in header_rows:  # 遍历所有标题行，这样我们可以得到可读性更强的标签。这并不是最快的方法，但可以保证不会有遗漏。
            if dkey in header_dict.values():  # 用的是字典的 values 方法，而不是遍历标题行的所有键值对。这一方法返回的是仅由字典的值组成的列表。还用到了 Python 的 in 方法，用来测试一个对象是否包含在某个列表中。对象是键，或缩写字符串，而列表是标题字典的值组成的列表（里面包含缩写短标题）。如果本行代码为真就找到了一个匹配行。
                new_row[header_dict.get('Label')] = dval  # 每找到一个匹配，都将其添加到 new_row 字典中。将字典的键设置为标题行中 Label 对应的值，也就是将短标题（Name 对应的值）替换为可读性更好的长标题（Label 对应的值），并将字典的值设置为数据行的值（dval）。
    new_rows.append(new_row)  # 将清洗过的新数据添加到新列表中,保证找到了所有的匹配，然后再运行后面的代码

print new_rows[0]
print '---'*20

# str_new_rows = str(new_row[0])
# print str_new_rows.split(',')

