# -*- coding:utf-8 -*-
"""
------
Filename:   T01-numpyTest01-ndaray的使用
date:   17/10/21
Description:    
    
------
"""
import numpy as np

# 创建数组
data1 = [6, 5.8, 23, 3.7]
arr1 = np.array(data1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 9, 10]]
arr2 = np.array(data2)

data3 = np.zeros(10)
data4 = np.empty((2, 3, 2))
data5 = np.arange(15)

# 数据类型
arr3 = np.array([1, 2, 3], dtype=np.float64)

arr4 = np.array([1, 2, 3], dtype=np.int32)

arr5 = np.array([1, 2, 3, 4, 5])
float_arr = arr5.astype(np.float64)

arr6 = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr6.astype(np.int32)

numberic_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50],  dtype=np.float64)

empty_uint32 = np.empty(8, dtype='u4')

# 数组与标量间的运算
arr7 = np.array([[1., 2., 3.], [4., 5., 6.]])

# 索引和切片
arr8 = np.arange(10)
arr_slice = arr8[5:8]
arr_slice[1] = 12345
arr_slice[:] = 64

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2d[0, 3]



"""输入
arr1
arr2
arr1.ndim
arr2.ndim
arr1.shape
arr2.shape
arr1.dtype
arr2.dtype
------------
arr3.dtype
arr4.dtype
arr5.dtype
float_arr.dtype
arr6.astype(np.int32)
numberic_strings.astype(float)
int_a

int_array.astype(calibers.dtype)

empty_uint32
------------
arr7
arr7 * arr7
1/arr7
------------
arr8
arr8[5]
arr8[5:8]
arr8[5:8] = 12
arr8

arr8
arr8

arr2d[2]
arr2d[0][2]
arr2d[0, 2]

"""