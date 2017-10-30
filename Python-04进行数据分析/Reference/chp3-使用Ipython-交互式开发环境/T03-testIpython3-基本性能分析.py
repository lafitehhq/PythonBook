# -*- coding:utf-8 -*-
"""
------
Filename:   T03-testIpython3-基本性能分析
date:   17/10/21
Description:    
    测试代码的基本性能：%prun和%run -p
------
"""

import numpy as np
from numpy.linalg import eigvals

def run_experiment(niter=100):
    K = 100
    results = []
    for x in xrange(niter):
        mat = np.random.randn(K, K)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results

some_results = run_experiment()
print 'Largest one we saw: %s' %np.max(some_results)



"""输入
①-③等效：
①：python -m cProfile -s cumulative T03-testIpython3-基本性能分析.py 
②：%prun -l 7 -s cumulative run_experiment()
③：%run -p -s cumulative T03-testIpython3-基本性能分析.py
"""