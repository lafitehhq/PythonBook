# -*-coding:utf8-*-

"""
Description：  
打开JSON文件并将其转换成由字典组成的列表

拓展：  
①：json库：https://docs.python.org/2/library/json.html  
②：Python json 库的 loads 函数接收字符串作为参数，不接收文件作为参数。Python csv 库的
reader 函数接收打开的文件作为参数
"""
import json  # 导入Python的json库

json_data = open('../../data/chp3/data-text.json').read()  # 内置的open函数打开 JSON 文件；调用了已打开文件的read 方法，用来读取该文件，并将读取的内容保存在变量 json_data中。打开文件，然后读取文件得到的是一个str（字符串）。

data = json.loads(json_data)  # json.loads() 将JSON字符串载入Python，并将输出保存在变量data中

for item in data:  # for循环遍历所有数据，并打印出每一项
    print item
