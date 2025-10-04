# -*- coding:utf8 -*-
import matplotlib.font_manager as fm
import os
import matplotlib
current_dir = os.path.dirname(os.path.realpath(__file__))
myfont = fm.FontProperties(fname='{current_dir}/plot_zh.ttf'.format(current_dir=current_dir))

import matplotlib.pyplot as plt

plt.clf()  # 清空画布
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel(u"横轴", fontproperties=myfont)
plt.ylabel(u"纵轴", fontproperties=myfont)
plt.title("pythoner.com", fontproperties=myfont)
plt.legend([u'图例'], prop=myfont)
plt.show()
