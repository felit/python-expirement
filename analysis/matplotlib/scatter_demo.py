import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 4, 5, 6, 7, 89, 6, 5, 12]
colors = np.random.rand(10)
area = np.pi * (15 * np.random.rand(N)) ** 2  # 0 to 15 point radiuses

plt.scatter(x, y,
            s=np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) * 50,
            c=colors,
            alpha=0.3,
            vmin=0.1,
            vmax=0.9,
            label="test scatter",
            # linewidths=[10, 20, 30, 40, 50, 60],
            edgecolors=[0.1, 0.2, 0.3, 0.4])
plt.grid(True)
plt.legend()
f = plt.subplot()
# f.bar(['2016-07-01', '2016-08-01', '2016-09-01'], [2, 3, 4])
f.plot(['2016-07-01', '2016-08-01', '2016-09-01'], [2, 3, 4])
plt.show()
