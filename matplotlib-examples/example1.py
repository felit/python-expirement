import numpy as np
import matplotlib.pyplot as plt
"""
matplotlib API包含有三层：
backend_bases.FigureCanvas : 图表的绘制领域
backend_bases.Renderer : 知道如何在FigureCanvas上如何绘图
artist.Artist : 知道如何使用Renderer在FigureCanvas上绘图
"""
import matplotlib
# 绘图、直方图、功率图、柱状图
x = np.arange(1, 5, 0.1)
y = np.sin(x)
z = np.cos(x)
print(x, y)
# [<matplotlib.lines.Line2D object at 0x10455cef0>]
line = plt.plot(x, y)
print(line)
print(dir(line))
# line.set_color("r")
# line.set_linewitdth(2.0)
print(plt.getp(line))
# plt.setp(line,color='g',linewitdth=2.0)
plt.plot(x, z)
plt.show()
