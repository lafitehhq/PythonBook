import json  # 导入Python的json库

json_data = open('../../data/chp3/data-text.json').read()  # 内置的open函数打开 JSON 文件；调用了已打开文件的read 方法，用来读取该文件，并将读取的内容保存在变量 json_data中

data = json.loads(json_data)  # json.loads() 将JSON 数据载入Python，并将输出保存在变量data中

for item in data:  # for循环遍历所有数据，并打印出每一项
    print item
