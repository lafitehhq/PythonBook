#-*-coding:utf-8_-*-

"""
Description:
用slate库读取PDF

拓展:


"""

import slate  # 导入slate库。

pdf = 'E:\Pycharm Workingspace\PythonBook\Python-03数据处理\Reference\data\chp5\EN-FINAL Table 9.pdf'  # 创建字符串变量，用于保存文件路径，一定要确保空格和大小写都正确

with open(pdf) as f:  # 将文件名字符串传入Python的 open函数
    doc = slate.PDF(f)  # 将打开的文件 f 传递给slate.PDF(f)，slate可以将PDF文件解析成可用的格式

for page in doc[:2]:  # 遍历文档doc的前两页并输出
    print page
