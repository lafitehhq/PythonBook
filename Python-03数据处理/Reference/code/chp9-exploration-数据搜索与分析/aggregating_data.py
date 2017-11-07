# -*- coding: utf-8 -*-

"""
Part 4 / 5
NOTE: This is a continuation of the IPython session working with
child labor and corruption indexes to determine correlation. Again, it
should not be used as a script, but instead an example of functions and
methods when exploring data.
"""
import json
import agate

country_json = json.loads(open('..\..\data\chp9\earth.json', 'rb').read())  # 使用 json 库来加载 .json 文件。如果你观察这个文件的话，会看到文件中保存了类型为字典的列表。
country_dict = {}

for dct in country_json:
    country_dict[dct['name']] = dct['parent']  # 遍历country_dict，将country 作为键、continent 作为值填充到字典中


def get_country(country_row):  # 创建函数：接受国家作为参数，返回它归属的大洲。这个函数使用了 Python 的字符串方法lower，将大写字母替换为小写形式。.json 文件包含的都是小写的国家名称。
    return country_dict.get(country_row['Country / Territory'].lower())

cpi_and_cl = cpi_and_cl.compute([('continent',  # 使用get_country 函数创建一个新的列，continent。沿用相同的表名称
#                                   agate.Formula(text_type, get_country)), ])
# print cpi_and_cl.column_names

for r in cpi_and_cl.rows:  # 有了大洲和国家数据。做一个快速的检查来确保没有遗漏任何东西
    print r['Country / Territory'], r['continent']

# no_continent = cpi_and_cl.where(lambda x: x['continent'] is None)
# for r in no_continent.rows:
#     print r['Country / Territory']
#
# cpi_and_cl = cpi_table.join(ranked, 'Country / Territory',
#                             'Countries and areas', inner=True)
# country_json = json.loads(open(
#     '..\..\data\chp9\earth-cleaned.json', 'rb').read())
#
# for dct in country_json:
#     country_dict[dct['name']] = dct['parent']
#
# cpi_and_cl = cpi_and_cl.compute([('continent',
#                                   agate.Formula(text_type, get_country)), ])
#
# for r in cpi_and_cl.rows:
#     print r['Country / Territory'], r['continent']
#
# grp_by_cont = cpi_and_cl.group_by('continent')
# grp_by_cont
#
# for cont, table in grp_by_cont.items():
#     print cont, len(table.rows)
#
# agg = grp_by_cont.aggregate([('cl_mean', agate.Mean('Total (%)')),
#                              ('cl_max', agate.Max('Total (%)')),
#                              ('cpi_median', agate.Median('CPI 2013 Score')),
#                              ('cpi_min', agate.Min('CPI 2013 Score'))])
#
# agg
# agg.print_table()
#
# agg.print_bars('continent', 'cl_max')
