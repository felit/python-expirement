# -*- coding:utf8 -*-
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

df1 = DataFrame({
    'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
    'data1': range(7)
})
print df1
df2 = DataFrame({
    'key': ['a', 'b', 'd'],
    'data2': range(3)
})
print pd.merge(df1, df2)
print pd.merge(df1, df2, on='key')
print pd.merge(df1, df2, left_on='data1', right_on='data2')
print pd.merge(df1, df2, left_on='data1', right_on='data2', how='outer')
print pd.merge(df1, df2, left_on='data1', right_on='data2', how='left')

# n*n
left = DataFrame({
    'key1': ['foo', 'foo', 'bar'],
    'key2': ['one', 'two', 'one'],
    'lval': [1, 2, 3]
})

right = DataFrame({
    'key1': ['foo', 'foo', 'bar', 'bar'],
    'key2': ['one', 'one', 'one', 'two'],
    'lval': [4, 5, 6, 7]
})
print pd.merge(left, right, on=['key1', 'key2'], how='outer')
print pd.merge(left, right, on=['key1', 'key2'], how='outer', suffixes=('_left', '_right'))
print pd.merge(left, right, on=['key1', 'key2'], how='outer', suffixes=('_left', '_right'), sort=True)
dd = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print dd.index


# 层次化索引
lefth = DataFrame({
    'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
    'key2': [2000, 2001, 2002, 2001, 2002],
    'data': np.arange(5.)
})
righth = DataFrame(
    np.arange(12).reshape((6, 2)),
    index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'], [2001, 2000, 2000, 2000, 2001, 2002]],
    columns=['event1', 'event2']
)

print righth
print pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
# 轴向连接
arr = np.arange(12).reshape((3, 4))
print arr
print np.concatenate([arr, arr], axis=1)
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
s4 = pd.concat([s1 * 5, s3])

print pd.concat([s1, s2, s3])
print pd.concat([s1, s2, s3], axis=1)
print pd.concat([lefth, righth])

print pd.isnull(pd.concat([lefth, righth]))
a = pd.concat([lefth, righth])
a[a is None] = 0
print a.replace(np.nan, 0)
print s4
# TODO 未完成
# 离散化和面元划分
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print cats
print cats.codes
print pd.value_counts(cats)