# -*- coding:utf8 -*-
import numpy as np

a = np.arange(16).reshape(4, 2, 2)
print a
print a.ndim, a.shape, a.size, a.dtype

# array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange, linspace, rand, randn, fromfunction, fromfile
print np.empty(20)
print np.empty_like(a)
print np.identity(10)
print np.eye(2, dtype=int)

arr = np.arange(40).reshape(2, 4, 5)
print arr.shape

a2 = np.array([[1, 2, 3, 4], [1, 2, 3]])
print a2.shape
print np.zeros((3, 4, 6))
print np.empty((4, 4, 9))
print np.eye(4)
print np.identity(4).astype(np.int16)