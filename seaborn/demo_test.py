# -*- coding:utf8 -*-
# %matplotlib inline
import pandas as pd
import seaborn as sns

boston = pd.read_csv("/Users/congsl/work/self/python-expirement/seaborn/data.csv")
boston.head(10)

sns.jointplot(x="CRIM", y="MEDV", data=boston)
sns.lmplot(x="CRIM", y="MEDV", data=boston)
sns.distplot(boston["TAX"])
sns.distplot(boston["TAX"], kde=False)
sns.distplot(boston["RM"], kde=False)
sns.distplot(boston["MEDV"], bins=100, kde=False)
sns.boxplot(boston["MEDV"], orient="v")
import math

boston["RM_int"] = boston["RM"].map(math.floor)  # 因为RM原始为连续型特征，首先对其取整
sns.boxplot(x="RM_int", y="MEDV", data=boston, orient="v")
sns.boxplot(x="RM_int", y="MEDV", hue="CHAS", data=boston, orient="v")
sns.countplot(x="RM_int", data=boston)
sns.countplot(x="RM_int", hue="CHAS", data=boston)
sns.kdeplot(boston["CRIM"])
sns.kdeplot(boston["ZN"])
sns.kdeplot(boston["NOX"], boston["LSTAT"])
sns.violinplot(x="RM_int", y="MEDV", data=boston)
sns.violinplot(x="RM_int", y="MEDV", hue="CHAS", data=boston, orient="v")
# sns.violinplot(x="RM_int", y = "MEDV", hue = "CHAS",split = True, data = boston)
sns.pairplot(boston[["CRIM", "NOX", "RM", "LSTAT", "MEDV"]])
import matplotlib.pyplot as plt

corr = boston.corr()  # 特征的相关系数矩阵
f, ax = plt.subplots(figsize=(10, 10))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, cmap=cmap, vmax=1.0,
            square=True, xticklabels=2, yticklabels=2,
            linewidths=.3, cbar_kws={"shrink": .5}, ax=ax)
plt.show()
