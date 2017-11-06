# -*- coding: utf-8 -*-

"""
Description:
    将下载的Excel文件原始数据转化为agate 库所接受的格式
拓展：
①：agate库可以使用一个标题列表、一个各数据列的类型列表和一个数据读取器（或可迭代的数据列表）来导入数据。
②：agate 库有文本、布尔、数字和日期 4 种列类型，如果数据的类型不确定，就使用文本类型。这里同样有内置的 TypeTester（http://agate.readthedocs.io/en/latest/api/data_types.html），可以用其猜测数据类型。
"""

import xlrd
import agate


workbook = xlrd.open_workbook('..\..\data\unicef\unicef_oct_2014.xls')  # 将Excel中的数据加载到变量workbook,工作表包含一个表单，叫作Child labour
print workbook.nsheets
print '---'*20

print workbook.sheet_names()
print '---'*20

sheet = workbook.sheets()[0]
print sheet.nrows  # nrows标识表单中共有多少列。
print '---'*20

print sheet.row_values(0)  # row_values允许选取一行数据，并且展示这行的值。此例子展示表单数据的标题，因为标题是Excel文件的第一行。
print '---'*20

for r in range(sheet.nrows):
    print r, sheet.row(r)  # 通过使用range和for遍历每一行数据，可以查看每一行数据。表单的row方法会返回数据的一些信息和每行数据的类型。
print '---'*20

title_rows = zip(sheet.row_values(4), sheet.row_values(5))  # 标题在第 4 行和第 5行。可以使用zip 来合并标题行
print title_rows
print '---'*20

# 标题数据当前是一个元组列表。agate库希望得到一个元组列表，其中第一个值为标题的字符串，这样需要将标题转换成字符串列表。
# 第一个列表生成式使用了元组的两个部分（通过元组索引）来拼接一个字符串。将每一个元组的值合并在一起，出于可读性的考虑，使用 ' '做间隔。
# 现在标题列表只由字符串组成——原来的元组不见了,使得标题变得有一些复杂，因为并不是每一个元组都有两个值。通过添加空格分隔创建了一些以空格为开始的标题，像'Female'。为了删除起始位置的空格
titles = [t[0] + ' ' + t[1] for t in title_rows]
print titles
print '---'*20

titles = [t.strip() for t in titles] # 为了删除起始位置的空格，在第二个迭代器中，使用 strip 字符串方法移除字符串最开始和最后的空格。现在标题变量有了整洁的字符串列表，能够很好地在agate库中使用。
print titles
print '---'*20

# 首先聚焦于国家的数据。想要避免意外地将不同类别的数据混合在一起。通过之前的代码输出，第 6 行至第 114 行是想要使用的。
# 使用row_values 方法来返回 xlrd 表单对象中这些行中的值。
country_rows = [sheet.row_values(r) for r in range(6, 114)]
print country_rows
print '---'*20

# 有了标题列表和数据列表，所以只需要定义导入 agate 库中的类型

from xlrd.sheet import ctype_text
import agate

text_type = agate.Text()
number_type = agate.Number()
boolean_type = agate.Boolean()
date_type = agate.Date()
example_row = sheet.row(6)
print example_row  # 通过打印来检查这一行的值看到有完好的数据。xlrd 会检查所有的数据，保证不会有空行数据的存在
print example_row[0].ctype  # 调用ctype和value属性来得到数据行中每一个元素的类型和值属性。
print example_row[0].value  # ctype 方法和 ctype_text 对象可以用来排序和展示给定样例数据行中的数据类型。
print ctype_text  # 使用 xlrd 库中的 ctype_text 对象可以匹配 ctype 方法返回的整数对象，映射它们到可阅读的字符串。这可以代替手动映射类型。
print '---'*20

# 知道哪些函数可以用来探索 Excel 列的数据类型，所以需要尝试为 agate 库创建一个类型列表,需要遍历数据行，使用ctype来映射列类型:
types = []

for v in example_row:
    value_type = ctype_text[v.ctype]  # 映射在探索每一行数据的 ctype 属性时找到的整数值到 ctype_text 字典中，使它们变得可读。现在 value_type 中保存了数据的列类型字符串（也就是文本、数字等）。
    if value_type == 'text':  # 使用 if 和 elif 语句以及 == 操作符将 value_type 和 agate 列类型匹配。之后，代码将相应的类型追加到列表中，继续下一个列类型。
        types.append(text_type)
    elif value_type == 'number':
        types.append(number_type)
    elif value_type == 'xldate':
        types.append(date_type)
    else:
        types.append(text_type)  # 如果这里没有类型匹配上，将文本列类型追加到列表中

print types
print titles
print '---'*20

# 构建了一个函数来接受一个空列表，遍历所有的列，并且创建一个包含数据集中所有列类型的列表。
# 在运行代码之后，我们就有了需要的类型、标题和数据列表。可以将标题和类型打包在一起，通过运行下面这行代码，将结果导入到 agate表中
# 当运行这段代码时，会看到 CastError，同时还有 Can not convert value “-” to Decimal for NumberColumn 这行错误信息。
# table = agate.Table(country_rows, titles, types)
print '---'*20


def remove_bad_chars(val):  # 定义函数来去除坏字符（例如整数列中的'-'字符）。
    if val == '-':  # 如果值与'-'相等，选择这个值准备替换。
        return None  # 如果值为'-'，返回 None。
    return val

cleaned_rows = []
for row in country_rows:
    cleaned_row = [remove_bad_chars(rv) for rv in row]  # 遍历country_rows 来创建一个新的清洗后的列表，包含合法的数据。
    cleaned_rows.append(cleaned_row)  # 创建一个cleaned_rows列表包含清洗后的数据（通过append 方法）。

table = agate.Table(cleaned_rows, titles, types)
print table
print '---'*20


# 因为想要复用清洗和改变类型的代码，所以把一些已经编好的代码转变成更加抽象和通用的辅助函数。
# 创建最后的清洗函数时，创建了一个新的列表，遍历所有行的数据，对每一行数据做了清洗，并为 agate 表返
def get_new_array(old_array, function_to_clean):  # 定义函数，让其接受两个参数：老的数据数组和清洗数据的函数
    new_arr = []
    for row in old_array:
        cleaned_row = [function_to_clean(rv) for rv in row]
        new_arr.append(cleaned_row)
    return new_arr  # 用更抽象的名称复用我们的代码。在函数的最后，返回新的清洗后的数组

cleaned_rows = get_new_array(country_rows, remove_bad_chars)  # 使用remove_bad_chars函数作为参数调用这个函数，保存清洗后的结果到cleaned_row

table = agate.Table(cleaned_rows, titles, types)
table.print_table(max_columns=7)
print table.column_names  # 检查列名称，这样知道要使用的是什么列。
print '--'*20


# 为表排序。通过对童工雇用率的总百分比的列排序，可以看到最过分的国家。
# 使用limit（http://agate.readthedocs.io/en/latest/api/table.html）函数来查看雇用率最高的10个国家。
most_egregious = table.order_by('Total (%)', reverse=True).limit(10)  # 链式调用 order_by 和 limit 方法来创建新的表。因为 order_by 会按从最小到最大来排序，所以我们使用 reverse 参数来让其从大到小排序。
for r in most_egregious.rows:  # 使用新表的 rows属性，遍历童工雇用情况最糟糕的10个国家。
    print r
print '--'*20

# 探究哪些国家的女童雇用率最高，再一次使用 order_by 和 limit 函数。这一次将它们应用到女童百分比数据列上
most_females = table.order_by('Female', reverse=True).limit(10)
for r in most_females.rows:
    print '{}: {}%'.format(r['Countries and areas'], r['Female'])
print '--'*20

# 可以使用 agate 表的 where 方法清除这些数据，这一方法类似于 SQL 中的 WHERE 语句，或者Python 中的 if语句。where 创建另外一个只包含符合条件的数据行的表。
female_data = table.where(lambda r: r['Female'] is not None)
most_females = female_data.order_by('Female', reverse=True).limit(10)
for r in most_females.rows:
    print '{}: {}%'.format(r['Countries and areas'], r['Female'])
print '--'*20


# 创建 female_data 表，其中使用了 Python 的 lambda 函数来保证每一行数据有 Female列存在。
# where 函数接受 lambda 函数返回的布尔值，并且只在值为真时将数据分离出来。
# 将只含有女性童工雇用数据的行分离出来后，我们使用相同的排序、截断和格式化技巧，来查看女童雇用率非常高的国家列表。
(lambda x: 'Positive' if x >= 1 else 'Zero or Negative')(0)  # 将lambda 函数放在第一对括号中，将要使用的变量作为x 放在第二对括号中。这个lambda 函数检查参数是否等于或大于 1。如果是，返回 Positive，否则返回 Zero or Negative
(lambda x: 'Positive' if x >= 1 else 'Zero or Negative')(4)

# 收到 NullComputationWarning 异常,异常意味着Place of residence (%) Urban 列中可能有一些空数据。
# table.columns['Place of residence (%) Urban'].aggregate(agate.Mean())  # 调用了表的 aggregate 方法，使用 agate.Mean() 统计学方法和列名称来返回列的数学均值
# col = table.columns['Place of residence (%) Urban']  # 假如想要找到城市童工雇用率的平均百分比。为此，我们来计算Place of residence (%) Urban这列数据的均值：
# table.aggregate(agate.Mean('Place of residence (%) Urban'))

# 再次使用 where 方法来聚焦于城市平均值
# 现得到了相同的值，这是因为 agate 在背后做了相同的事情（去除空列，计算剩下数据的平均值）。place of residence列的最小值（Min）、最大值（Max）和均值（Mean）。
has_por = table.where(lambda r: r['Place of residence (%) Urban'] is not None)
print has_por.aggregate(agate.Mean('Place of residence (%) Urban'))
print '--'*20

# 假如想要找到每行数据中农村童工雇用率大于 50% 的数据。
# agate 库有一个 find 方法，使用条件语句来找到第一个匹配的数据。
# 返回的那行数据就是第一个匹配到的数据
first_match = has_por.find(lambda x: x['Rural'] > 50)
print first_match['Countries and areas']
print '--'*20

# 要查看童工雇用率最高国家的排名，可以使用 Total (%) 列数据进行排序。
# 在将这个数据集和其他数据集合并之前，想要一个清晰可见的排序后列数据来比较合并后的数据。
# 因为想要雇用率更高的国家出现在列表前面，所以需要使用参数 reverse=True逆序排序（http://agate.readthedocs.io/en/latest/cookbook/rank.html#rank-descending）。
ranked = table.compute([('Total Child Labor Rank', agate.Rank('Total (%)', reverse=True)),])
for row in ranked.order_by('Total (%)', reverse=True).limit(20).rows:
    print row['Total (%)'], row['Total Child Labor Rank']

print '---'*20

# 另一种方式来计算排名，可以用逆百分比创建一列数据。相对于使用每个国家雇用童工的百分比数据，可以使用普通儿童的占比来进行计算。
# 使用agate.Rank()方法时，不需要 reverse 参数
def reverse_percent(row):  # 创建一个新的函数来计算并返回给定数据的逆百分比。
    return 100 - row['Total (%)']
ranked = table.compute([('Children not working (%)',
                             agate.Formula(number_type, reverse_percent)),
                            ])  # 使用 agate 库的 compute 方法，传递一个列表作为参数，并返回新的数据列。列表中的每一个元素必须是元组对象，而元组的第一个元素包含列名称，第二个元素用来计算新的列。在这里，我们使用 Formula 类，其同样需要一个 agate 类型，同函数一起，创建一个列表值。

ranked = ranked.compute([('Total Child Labor Rank',
                              agate.Rank('Children not working (%)')),
                           ])  # 用Children not working (%)列的数据来创建有适当排序的Total Child Labor Rank列。可以看到，compute是一个非常好用的工具，它基于一个数据列（或多个数据列）来计算一个新的数据列。


for row in ranked.order_by('Total (%)', reverse=True).limit(20).rows:
    print row['Total (%)'], row['Total Child Labor Rank']




