# -*- coding: utf-8 -*-

"""
Description:
    使用标准数据类型打开和写文件。
    使用本地文件作为输入和输出时，你需要确保脚本可以每天运行在相同的机器上，或者可
以简单地与输入和输出文件一起迁移。随着脚本的开发，很可能需要同时移动并改变脚本
和所用文件。

"""
from csv import reader, writer


def read_local_file(file_name):
    if '.csv' in file_name:  # 测试文件是否适合使用 csv 模块打开。如果文件以 .csv 结尾，之后可以使用CSV 读取器来打开它。
        rdr = reader(open(file_name, 'rb'))
        return rdr
    return open(file_name, 'rb')  # 如果没有返回 CSV 读取器，这段代码返回打开的文件。如果想要根据文件扩展类型，构建一系列不同的方式来打开并解析文件，也可以做到（例如，为 JSON 文件使用 json模块，或者为PDF文件使用 pdfminer）。


def write_local_file(file_name, data):
    with open(file_name, 'wb') as open_file:  # 使用with...as 返回 open 函数的输出，将其赋值给open_file 变量。当缩进的代码块结束时，Python会自动地关闭文件。
        if type(data) is list:  # 如果正在处理列表，这一行代码使用 CSV 输出器输出每一行列表对象为一行数据。如果有字典，可以使用DictWriter 类。
            wr = writer(open_file)
            for line in data:
                wr.writerow(line)
        else:
            open_file.write(data)  # 要将原始数据写到文件中。此外，根据数据类型的不同，还可以写不同的代码


