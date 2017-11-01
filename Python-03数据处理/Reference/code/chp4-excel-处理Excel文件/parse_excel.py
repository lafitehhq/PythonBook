#-*-coding:utf-8_-*-

"""
Description：
利用xlrd处理Excel文件

拓展：
①：处理 Excel文件主要有三个库。
    • xlrd：读取Excel文件。
    • xlwt：向Excel文件写入，并设置格式。
    • xlutils：一组Excel高级操作工具（需要先安装 xlrd 和xlwt）。
"""

import xlrd

# xlrd.open_workbook用于打开excel文件
book = xlrd.open_workbook("../../data/chp4/SOWC 2014 Stat Tables_Table 9.xlsx")

# 用法1：查询所用工作表名字
for sheet in book.sheets():  # 查看工作表都有哪些名字
    print sheet.name  # 打印工作表的名字
print '---'*10

# 用法2：打开某工作表得到工作表内容
sheet = book.sheet_by_name("Table 9 ")  # book.sheet_by_name(somename)访问工作表的名字。注意：工作表名在结尾有一个多出来的空格

# 2.1返回表格总行数
print sheet.nrows
print '---'*10

# 2.2打印表格内容，用字典表示（不太实用）
print dir(sheet)  # 发现一个叫作 nrows 的方法可用这个方法来遍历所有行
print '---'*10

# 2.3sheet类型
print type(sheet)  # <class 'xlrd.sheet.Sheet'>
print '---'*10

# 2.4利用索引查找所有行的值
for i in range(sheet.nrows):  # 利用i作为索引来查找对应行的值,for 循环的次数等于工作表的长度,得到的每一行是一个列表
    print sheet.row_values(i)
print '---'*10

# 2.5利用索引查找对应行及列的值
# for i in xrange(sheet.nrows):
#     row = sheet.row_values(i)  # 将每一行内容组成的列表保存到 row 变量中
#     for cell in row:  # 遍历列表中的每一个元素，也就是当前行的每一个单元格
#         print cell  # 输出单元格的值
# print '---' * 10

# 2.6利用索引得到具体某行的值
count = 0
for i in xrange(sheet.nrows):
    if count < 20:  # 遍历前20行内容，找到国家名字开始出现的那一行。
        if i > 14:  # 从国家名字出现的那一行开始输出每行的内容
            row = sheet.row_values(i)
            print i, row
        count += 1
print '---' * 10

# 2.7利用索引将某行作为字典的列
count = 0
data = {}  # 创建一个空字典来保存数据。
for i in xrange(sheet.nrows):
    if count < 10:
        if i > 14:
            row = sheet.row_values(i)
            country = row[1]  # row[1]提取出遍历每一行的国家名字。
            data[country] = {}  # data[country] 将国家设为 data 字典的键，对应的值设为另一个字典，接下来要将数据保存在这个字典里
            count += 1
print data  # 输出data 字典
print '---' * 10

# 2.8.# 用索引访问某行某列1.0
count = 0
data = {}
for i in xrange(14, sheet.nrows):  # for 循环从工作表第 14 行开始。这一行代码从 i的值为14开始循环
    row = sheet.row_values(i)
    country = row[1]
    data[country] = {  # 将字典扩展成很多行，可以填入其他数据点
        'child_labor': {  # 创建了child_labor 键，并把它的值设为另一个字典
            'total': [],  # 字典又包含了几个字典，字典的键是字符串，说明了保存的数据内容。每一个键对 应的值都是列表。
            'male': [],
            'female': [],
        },
        'child_marriage': {
            'married_by_15': [],
            'married_by_18': [],
        }
    }
print data['Afghanistan']  # 输出与Afghanistan 键对应的值
print '---' * 10

# 2.9用索引访问某行某列2.0
data = {}
for i in xrange(14, sheet.nrows):  # # 从第14行开始，因为这是国家数据的起点。

    # Start at 14th row, because that is where the countries begin
    row = sheet.row_values(i)  # 用row_values()方法接收一个索引数字，返回对应行的值来获取每一行的值

    country = row[1]

    data[country] = {
        'child_labor': {
            'total': [row[4], row[5]],
            'male': [row[6], row[7]],
            'female': [row[8], row[9]],
        },
        'child_marriage': {
            'married_by_15': [row[10], row[11]],
            'married_by_18': [row[12], row[13]],
        }
    }
    if country == "Zimbabwe":
        break

print data['Afghanistan']

