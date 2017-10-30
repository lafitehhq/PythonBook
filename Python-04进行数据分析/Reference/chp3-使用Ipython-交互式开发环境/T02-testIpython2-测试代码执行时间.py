# -*- coding:utf-8 -*-
"""
------
Filename:   T02-testIpython2-测试代码执行时间
date:   17/10/21
Description:    
    测试代码的执行时间：%time和%timeit
------
"""

strings = ['foo',  'foobar', 'baz', 'qux', 'python’, ’Guido Van Rossum'] * 100000

method1 = [x for x in strings if x.startswith('foo')]
method2 = [x for x in strings if x[:3] == 'foo']






"""输入&输出
%time method1
CPU times: user 3 µs, sys: 1e+03 ns, total: 4 µs
Wall time: 8.11 µs

%time method2
CPU times: user 4 µs, sys: 1 µs, total: 5 µs
Wall time: 8.11 µs

%timeit method1
10000000 loops, best of 3: 26.7 ns per loop

%timeit method2
10000000 loops, best of 3: 26.3 ns per loop
"""