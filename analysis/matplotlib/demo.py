# -*- coding:utf8 -*-
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from numpy.random import random
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.plot(random(50).cumsum(), 'k--')
plt.plot([1.5, 3.5, -2, 1.6])
ax1.hist(random(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * random(30))

fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.1, hspace=0.1)

plt.show()

