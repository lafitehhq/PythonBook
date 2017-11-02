# -*- coding: utf-8 -*-

""" 
@File: data_format_数据格式化.py 
@Version:
@Description:
"""

from datetime import datetime


start_string = '{}/{}/{} {}:{}'.format(  # 创建一个字符串模板（base string），用于解析多个数据条目中的数据。本行代码使用的是美国人常用的日期格式：月、日、年，然后是小时和分钟。
zipped_data[0][8][1], zipped_data[0][7][1], zipped_data[0][9][1],  # 数据读取格式如下：zipped_data[ 第一个数据条目 ][ 数据行编号（由 enumerate 得到）][ 数据本身 ]。利用第一个数据条目测试，索引号为 8 的那一行是月，索引号为 7 的那一行是日，索引号为9的那一行是年。每个元组的第二个元素（[1]）是我们需要的数据。
zipped_data[0][13][1], zipped_data[0][14][1])
print start_string

start_time = datetime.strptime(start_string, '%m/%d/%Y %H:%M') # 数据读取格式如下：zipped_data[ 第一个数据条目 ][ 数据行编号（由 enumerate 得到）][ 数据本身 ]。利用第一个数据条目测试，索引号为 8 的那一行是月，索引号为 7 的那一行是日，索引号为9的那一行是年。每个元组的第二个元素（[1]）是我们需要的数据。
print start_time

end_time = datetime(  # 将整数直接传递给 datetime 模块的 datetime 类，生成一个日期对象。传入整数作为参数，整数之间用逗号隔开。
int(zipped_data[0][9][1]), int(zipped_data[0][8][1]),  # 由于 datetime 只接受整数，本行代码将所有的数据转换成整数。datetime 输入参数的顺序是年、月、日、时、分，所以我们必须相应调整数据的顺序。
int(zipped_data[0][7][1]), int(zipped_data[0][15][1]),
int(zipped_data[0][16][1]))
print end_time

duration = end_time - start_time  # 用结束时间减去开始时间，计算出采访时长。
print duration  # 打印一个新的 Python 日期类型。这是一个 timedelta 对象。timedelta 会给出两个时间对象的时间差，还可用于改变时间对象
print duration.days  # 利用内置的 days属性来查看timedelta对象里包含了多少天
print duration.total_seconds()  # 调用timedelta 对象的 total_seconds方法，计算时间差包含多少秒。结果精确到微秒

minutes = duration.total_seconds() / 60.0  # 计算分钟数，因为 timedelta对象没有分钟属性
print minutes

print end_time.strftime('%m/%d/%Y %H:%M:%S')  # strftime 只能输入一个参数，就是你希望显示的日期格式。本行代码输出美国标准时间格式

print start_time.ctime()  # datetime 对象有一个 ctime方法，可以根据C 语言的 ctime 标准输出datetime对象。

print start_time.strftime('%Y-%m-%dT%H:%M:%S')  # datetime 对象可以用你能想到的任意格式输出字符串。本行代码用的是 PHP语言常用的时间格式。如果你需要用特殊字符串格式与 API 交互，datetime 模块可以帮到你。
