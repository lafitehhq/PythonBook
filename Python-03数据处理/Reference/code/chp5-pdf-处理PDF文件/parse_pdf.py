#-*-coding:utf-8_-*-

# Todo

import slate

pdf = '/Users/lafitehhq/PycharmProjects/PythonBook/Python-03数据处理/Reference/data/chp5/en-final-table9.txt'

with open(pdf) as f:
    doc = slate.PDF(f)

for page in doc[:2]:
    print type(page)
