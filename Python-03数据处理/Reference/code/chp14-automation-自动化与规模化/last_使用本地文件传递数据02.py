# -*- coding: utf-8 -*-

"""
Description:
    这段代码返回最近使用的文件夹，但是如果想要返回整个以最近使用文件开始的文件列
表，可以直接修改代码，不返回第一个索引，而是返回整个列表或一个切片。

"""
import os

def get_latest(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder)]  # 使用 Python 内置的 os 模块列出每一个文件（listdir 方法），之后使用 path 模块的join 方法创建一个长字符串，表示一个完整的文件路径。这是获取文件夹中所有文件的一种简单方式，只需要传递一个字符串（文件夹路径）。
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)  # 通过最后修改时间来为文件排序。因为 files 是一个列表，所以可以调用 sort 方法，并且给它一个键作为排序的依据。这段代码传递完整的文件路径给 getmtime 函数，这是 os 模块“获取修改时间”的方法。reverse 参数确保最近的文件出现在列表的顶部
    return files[0]  # 返回最近的文件。
