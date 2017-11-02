"""
Description:
合并不同的数据集，并希望保存每一条重复数据

"""

from csv import DictReader  # 用到DictReader模块解析想要的所有字段。

mn_data_rdr = DictReader(open('../../data/unicef/mn.csv', 'rb'))
mn_data = [d for d in mn_data_rdr]


def combine_data_dict(data_rows):  # 定义函数的作用是将 data_rows合并，然后返回一个字典
    data_dict = {}  # 定义一个新的数据字典，用于函数的返回值
    for row in data_rows:
        key = '%s-%s' % (row.get('HH1'), row.get('HH2'))  # 利用类群编号、家庭编号和家庭成员编号创建一个唯一键，与之类似，本行代码也创建一个唯一键。“HH1”代表类群编号，“HH2”代表家庭编号。本行代码用这两个编号来表示唯一家庭。
        if key in data_dict.keys():
            data_dict[key].append(row)  # 如果已经添加过这个家庭，本行代码将当前数据行添加到数据列表中
        else:
            data_dict[key] = [row]  # 如果这个家庭尚未添加，本行代码新建一个列表，列表元素为当前数据行。
    return data_dict  #  在函数末尾，返回新的数据字典。

mn_dict = combine_data_dict(mn_data)  # 本行代码将新生成的字典命名为mn_dict，可以利用这个字典来查看有多少个唯一家庭，以及每个家庭分别做了多少份调查。

print len(mn_dict)
