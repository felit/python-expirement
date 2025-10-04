#-*- coding:utf8 -*-
# https://blog.csdn.net/zhousishuo/article/details/75330506
# https://randyzwitch.com/creating-stacked-bar-chart-seaborn/
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
import seaborn as sns
# %matplotlib inline

#Read in data & create total column
stacked_bar_data = pd.read_csv("/Users/congsl/work/self/python-expirement/seaborn/py_trans.csv")
stacked_bar_data["total_cores"] = stacked_bar_data.rmb_cores + stacked_bar_data.cis_cores

#Set general plot properties
sns.set_style("white")
sns.set_context({"figure.figsize": (24, 10)})

#Plot 1 - background - "total" (top) series
sns.barplot(x = stacked_bar_data.logTime, y = stacked_bar_data.total_cores, color = "red")

#Plot 2 - overlay - "bottom" series
bottom_plot = sns.barplot(x = stacked_bar_data.logTime, y = stacked_bar_data.cis_cores, color = "#0000A3")
#图例
topbar = plt.Rectangle((0,0),1,1,fc="red", edgecolor = 'none')
bottombar = plt.Rectangle((0,0),1,1,fc='#0000A3',  edgecolor = 'none')
l = plt.legend([bottombar, topbar], ['cis total_cores', 'rmb total_cores'], loc=1, ncol = 2, prop={'size':16})
l.draw_frame(False)

#Optional code - Make plot look nicer
sns.despine(left=True)
bottom_plot.set_ylabel("total_cores")
# bottom_plot.set_xlabel("logTime")
bottom_plot.set_xlabel(u"中文logTime")
bottom_plot.set_xticklabels(stacked_bar_data.logTime, rotation=30, fontsize='small')
plt.show()
import matplotlib
print sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])