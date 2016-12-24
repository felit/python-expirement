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
print pd.concat([lefth, righth])