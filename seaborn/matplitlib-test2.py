import numpy as np
import matplotlib.pyplot as plt
size = 5
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)
d = np.random.random(size)
x = np.arange(size)

total_width, n = 0.8, 6     # 有多少个类型，只需更改n即可
width = total_width / n
x = x - (total_width - width) / 2
# 多个柱状图
align = "edge"
plt.bar(x, a,  width=width, label='a',align=align)
plt.bar(x + width, b, width=width, label='b',align=align)
plt.bar(x + 2 * width, c, width=width, label='c',align=align)
plt.legend()
plt.show()