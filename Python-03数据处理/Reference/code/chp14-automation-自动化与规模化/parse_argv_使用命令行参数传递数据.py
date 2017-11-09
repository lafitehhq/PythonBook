# -*- coding: utf-8 -*-

from import_config import get_config
import sys


def main(env):
    config = get_config(env)
    print config


if __name__ == '__main__':
    if len(sys.argv) > 1:  # 内置的 sys 模块，帮助完成系统任务，包括解析命令行参数。如果命令行参数列表的长度大于 1，这里存在额外的参数。第一个参数永远保存着脚本的名称（所以如果参数长度为1，脚本名称是唯一的参数）。
        env = sys.argv(1)  # 为了得到参数的值，传递参数的索引到 sys 模块的 argv 方法。这行代码设置 env 为参数的值。记住，argv 方法的索引 0 永远是 Python 的脚本名称，所以从索引 1 开始解析参数
    else:
        env = 'TEST'
    main(env)  # 使用解析后的参数，根据命令行参数修改代码。
