import numpy as np
import matplotlib.pyplot as plt
#标准正态分布
x = np.linspace(-5, 5, 2000)
y = (1 / (np.sqrt(2 * np.pi))) * (np.exp(-(x ** 2) / 2))
plt.plot(x, y, 'r-', linewidth=2)
plt.show()