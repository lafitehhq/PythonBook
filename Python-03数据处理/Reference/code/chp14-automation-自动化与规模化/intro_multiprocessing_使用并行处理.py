# -*- coding: utf-8 -*-

"""
拓展：
①：使用多重处理的时候，你通常会有一个管理者进程和一堆子进程。你可以传递参数给子进
程，可以使用共享内存和共享变量。这使你能够确定如何利用和架构 multiprocessing。根
据脚本的需要，你或许想要让管理器运行脚本中一系列的逻辑，同时使用子进程运行高延
迟或长时间运行的部分代码。
②：共 享 锁 对 象（https://docs.python.org/2/library/threading.html#lock-objects）
提供了同步执行多个进程的能力，同时能保护内部逻辑的特定区域。有效
使用它们的一个方式是直接放置锁逻辑到 with（https://docs.python.org/2/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement）
语句中


"""

from multiprocessing import Process, Manager  # 从内置的 multiprocessing库导入 Process 和Manager 类，来帮助我们管理进程
import requests

ALL_URLS = ['google.com', 'bing.com', 'yahoo.com',
            'twitter.com', 'facebook.com', 'github.com',
            'python.org', 'myreallyneatsiteyoushouldread.com']


def is_up_or_not(url, is_up, lock):  # 定义主要 worker 函数 is_up_or_not，培训需要 3 个参数：一个 URL、一个共享列表和一个共享锁。其中的列表和锁是在所有的进程间共享的，让其中的每一个进程能够修改或使用它们。
    resp = requests.get('http://www.isup.me/%s' % url)  # 使用requests 检查 isup.me，判定给定的URL当前是否在线并且可用
    if 'is up.' in resp.content:  # 测试是否可以在页面中找到文本“is up.”。如果文本存在，这个 URL就是我们想要的。
        is_up.append(url)
    else:
        with lock:  # 通过 with 代码块调用锁的 acquire 方法。这会得到锁，继续执行下面缩进的代码，然 后 在 代 码 块 的 最 后 释 放 锁。
            # 锁(http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/)是阻塞的，并且只
            # 能在代码中需要阻塞时使用（举个例子，如果你需要确保只有一个进程运行一组特殊的逻辑，比如检查一个共享值是否变化，或是否到达了一个终止点）。
            print 'HOLY CRAP %s is down!!!!!' % url


def get_procs(is_up, lock):  # 当生成进程时，传递共享的锁和列表到函数中使用。
    procs = []
    for url in ALL_URLS:
        procs.append(Process(target=is_up_or_not,
                             args=(url, is_up, lock)))  # 通过传递关键参数创建一个进程对象：目标（即，我应该执行哪个函数）和参数（即，使用什么参数）。这行代码追加所有的进程到一个列表，这样我们可以在一个地方管理它们。
    return procs


def main():
    manager = Manager()  # 初始化Manager 对象，这帮助我们管理共享的对象和进程间的日志。
    is_up = manager.list()  # 创建一个共享列表对象，跟踪每个站点的状态。每一个进程都能改变这个列表。
    lock = manager.Lock()  # 创建一个共享的锁对象，如果一个站点中不存在“is up”，停止并且宣布它。如果这些是我们管理的所有站点，我们可能有了一块重要的业务逻辑来处理紧急情况，也因此有了“停止所有程序”的理由。
    for p in get_procs(is_up, lock):  # 分别开始由函数 get_proc 返回的每一个进程。一旦它们开始执行，join 方法会让Manager对象和所有的子进程通信，直到最后一个进程完成。
        p.start()
        p.join()
    print is_up

if __name__ == '__main__':
    main()
