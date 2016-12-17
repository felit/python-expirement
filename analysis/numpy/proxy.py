# -*- coding:utf8 -*-
import numpy as np

arr = np.loadtxt('proxy.csv', delimiter=',', dtype='string')
print arr.size
# 维度:一维数据(1) 二维数据(2)、三维数据(3)、多维数据(n)
print arr.ndim
# 各个维度的数量
print arr.shape
# np.savetxt('proxy2.txt',arr,delimiter=',')
np.savez('proxy2.txt',arr)

print arr
arr2 = np.random.randn(7, 4)
print arr2
print arr2[3:, :3]
arr2[arr2 < 0] = 0
print arr2
print arr2.T
print np.dot(arr2.T, arr2)
