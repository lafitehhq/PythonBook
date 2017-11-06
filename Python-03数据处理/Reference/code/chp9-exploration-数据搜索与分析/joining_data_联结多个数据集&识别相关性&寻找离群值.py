# -*- coding: utf-8 -*-

"""
Description:
    政府腐败（或政府被认为有可能存在腐败）会不会影响童工雇用率
    通过国际公开腐败感指数（Transparency International’s Corruption Perceptions Index）数据集，并决定与 UNICEF 童工数据做比对。
"""
import agate
import xlrd

from xlrd.sheet import ctype_text  # 再一次使用 xlrd 来导入 Excel 数据，并且复用在之前编写的解析标题和为agate 库准备数据的代码


text_type = agate.Text()
number_type = agate.Number()
boolean_type = agate.Boolean()
date_type = agate.Date()


def remove_bad_chars(val):
    if val == '-':
        return None
    return val

# 创建函数 get_types，它接受一行数据，为 agate 库输出一个类型列表。
# 编写了get_table 函数，函数中使用了 Python内置的异常处理
def get_types(example_row):
    types = []
    for v in example_row:
        value_type = ctype_text[v.ctype]
        if value_type == 'text':
            types.append(text_type)
        elif value_type == 'number':
            types.append(number_type)
        elif value_type == 'xldate':
            types.append(date_type)
        else:
            types.append(text_type)
    return types


workbook = xlrd.open_workbook('..\..\data\unicef\unicef_oct_2014.xls')
sheet = workbook.sheets()[0]

title_rows = zip(sheet.row_values(4), sheet.row_values(5))
titles = [t[0] + ' ' + t[1] for t in title_rows]
titles = [t.strip() for t in titles]

country_rows = [sheet.row_values(r) for r in range(6, 114)]
cleaned_rows = []

for row in country_rows:
    cleaned_row = [remove_bad_chars(rv) for rv in row]
    cleaned_rows.append(cleaned_row)

example_row = sheet.row(6)
types = get_types(example_row)

table = agate.Table(cleaned_rows, titles, types)
ranked = table.compute([('Total Child Labor Rank',
                         agate.Rank('Total (%)', reverse=True)), ])


cpi_workbook = xlrd.open_workbook(
    '..\..\data\chp9\corruption_perception_index.xls')
cpi_sheet = cpi_workbook.sheets()[0]

for r in range(cpi_sheet.nrows):
    print r, cpi_sheet.row_values(r)
print '---'*20


cpi_title_rows = zip(cpi_sheet.row_values(1), cpi_sheet.row_values(2))
cpi_titles = [t[0] + ' ' + t[1] for t in cpi_title_rows]
cpi_titles = [t.strip() for t in cpi_titles]
cpi_rows = [cpi_sheet.row_values(r) for r in range(3, cpi_sheet.nrows)]

def get_table(new_arr, types, titles):
    try:  # try 代码块定义了代码可能抛出异常。try 关键字后面永远跟着一个冒号，并且单独占据一行空间。下面一行或者几行的代码，是一个 Python 的 try 代码块，使用4个空格缩进。
        table = agate.Table(new_arr, titles, types)
        return table  # 返回传入参数的整数形式。当参数是类似于 1 或者 4.5 的值时，这不会有问题。如果参数的值是'-' 或者'foo'，这会抛出一个 ValueError异常。
    except Exception as e:  # 开始 except 代码块，定义需要捕获的异常类型。这一行同样使用一个冒号作为结束，指定我们想要捕获一个 ValueError 异常（这样 except 代码块会只捕获ValueError 异常）。这个代码块和下面的代码只在 try 语句抛出了这行代码中指定的异常时才会执行。
        print e
print '---'*20

cpi_types = get_types(cpi_sheet.row(3))  # 使用新函数将腐败指数数据导入到Python
print cpi_titles
cpi_table = get_table(cpi_rows, cpi_types, cpi_titles)
print cpi_table
print '---'*20

# 展示处理重复列名称
cpi_titles[0] = cpi_titles[0] + ' Duplicate'
cpi_table = get_table(cpi_rows, cpi_types, cpi_titles)  # 新函数 get_table 会看到抛出的错误，而不是函数完全中断。重复的标题可能意味着 = 标题列表中有一些坏标题

cpi_and_cl = cpi_table.join(ranked, 'Country / Territory',  # agate 库的 join 方法允许传递 inner=True 参数，这会使函数仅作内联结，只保留匹配的行，不会在联结后有空值行。
                            'Countries and areas', inner=True)  # 尝试联结童工数据和新规整后的 cpi_table。查看这两个表时可以将它们通过国家 / 领土的名称匹配在一起。在 cpi_table 中有 Country/Territory 列，同时，在童工数据中，有Counties and areas列

cpi_and_cl.print_table()
print '---'*20

print len(cpi_and_cl.rows)
print len(cpi_table.rows)
print len(ranked.rows)
print '---'*20


# 将匹配行放到新表 cpi_and_cl 中。通过打印几个值来查看这张表，同时研究新的联结后的列
cpi_and_cl.column_names
for r in cpi_and_cl.order_by('CPI 2013 Score').limit(10).rows:
    print '{}: {} - {}%'.format(r['Country / Territory'],
                                r['CPI 2013 Score'], r['Total (%)'])
print '---'*20


# 1.5计算相关系数（例如皮尔森相关系数）告诉数据是否关联，以及一个因子是否会影响另一个因子。
import numpy
# print numpy.corrcoef(cpi_and_cl.columns['Total (%)'].values(),  # 得到了类似于之前曾见到的CastError异常的错误。因为numpy需要浮点型数据，而不是小数型，所以我们需要将数字转换回浮点数。我们可以使用列表生成式做这个转换
#               cpi_and_cl.columns['CPI 2013 Score'].values())[0, 1]

print numpy.corrcoef(  # 输出显示出一些轻微的负相关
    [float(t) for t in cpi_and_cl.columns['Total (%)'].values()],
    [float(s) for s in cpi_and_cl.columns['CPI 2013 Score'].values()])[0, 1]
print '---'*20


# 1.6.寻找离群值
# 有两种方法可以做到：一是使用标准差，第二个是使用绝对中位差。

import agatestats

# 方法1：使用标准差
# 当使用 Total (%) 列，尝试使用 3作为标准差识别离群值时，得到了和当前表完全匹配的一张表。这不是我们想要的结果。
# 当使用 5 作为差值界限时，并没有看到数据的变化则显示并不是常规的分布。
std_dev_outliers = cpi_and_cl.stdev_outliers(
    'Total (%)', deviations=3, reject=False)  # 使用童工雇用数据的 Total (%) 列和 agate-stats stdev_outliers 方法来查看数据中是否含有容易找到的标准差离群值。我们将这个方法的输出赋值给一个新的表std_dev_outliers。我们使用参数 reject=false 来告诉函数我们希望看到离群值。如果我们设置reject 等于True，将会得到没有离群值的数据。
print len(std_dev_outliers.rows)  # 查看发现了多少行离群值（这张表共有94行数据）。

std_dev_outliers = cpi_and_cl.stdev_outliers(
    'Total (%)', deviations=5, reject=False)  # 提高偏差的大小，减少离群值的数量。（deviations=5。）
print len(std_dev_outliers.rows)

# 方法2：使用平均绝对偏差检查Total (%)列数据的偏差
mad = cpi_and_cl.mad_outliers('Total (%)')
for r in mad.rows:
    print r['Country / Territory'], r['Total (%)']
