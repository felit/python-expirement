import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy import stats

# https://docs.scipy.org/doc/scipy-1.11.1/reference/generated/scipy.stats.norm.html#scipy.stats.norm
# Python学习-Scipy库统计操作(随机变量、概率密度、累积分布密度、期望、方差、描述性统计(最大最小值、均值、方差、偏差、峰度)、核密度估计): https://blog.csdn.net/weixin_41387192/article/details/110186684
# norm的方法： 'a', 'b', 'badvalue', 'cdf', 'entropy', 'expect', 'extradoc', 'fit', 'fit_loc_scale', 'freeze', 'generic_moment', 'interval', 'isf', 'logcdf', 'logpdf', 'logsf', 'mean', 'median', 'moment', 'moment_type', 'name', 'nnlf', 'numargs', 'pdf', 'ppf', 'random_state', 'rvs', 'sf', 'shapes', 'stats', 'std', 'support', 'var', 'vecentropy', 'xtol'
# scipy#API  统计值、描述统计
# Python Scipy stats.kurtosis()用法及代码示例: https://vimsky.com/examples/usage/scipy-stats-kurtosis-function-python.html
# scipy.stats常见概率分布-正态分布与泊松分布: https://blog.csdn.net/qq_34184505/article/details/127410509
print(norm.mean(), norm.std(), norm.var())


def norm_test():
    x = np.linspace(-1.5, 1.5, 100)
    labels = []
    f_list = [stats.norm.pdf, stats.norm.cdf, stats.norm.ppf]
    plt.figure(dpi=150)
    for f in f_list:
        labels.append(f)
        y = f(x, loc=0, scale=0.5)  # 标准正态分布，均值0，标准差0.5
        plt.tick_params(axis='both', labelsize=14)
        plt.plot(x, y)
    plt.legend(labels=['pdf', 'cdf', 'ppf'], loc='best')
    plt.title("Normal distribution")


def norm_2():
    x = np.linspace(-5, 5, 1000)
    labels = []
    mu_list = [0, 0, 0, -2]
    sigma_list = [0.2, 1.0, 5.0, 0.5]
    plt.figure(dpi=150)
    for mu, sigma in zip(mu_list, sigma_list):
        labels.append('μ={}, σ²={}'.format(mu, sigma))
        y = stats.norm.pdf(x, loc=mu, scale=math.sqrt(sigma))
        plt.axis([-5, 5, 0, 1.0])
        plt.tick_params(axis='both', labelsize=14)
        plt.plot(x, y)
    plt.legend(labels=labels, loc='best')


"""
stats.norm主要公共方法如下:
    rvs:随机变量（就是从这个分布中抽一些样本）
    pdf：概率密度函数。
    cdf：累计分布函数
    sf：残存函数（1-CDF）
    ppf：分位点函数（CDF的逆）
    isf：逆残存函数（sf的逆）
    stats:返回均值，方差，（费舍尔）偏态，（费舍尔）峰度。
    moment:分布的非中心矩。
"""
"""
loc 均值
scale：标准差
"""


# r = norm.rvs(loc=30,size=100,scale=100)
def first():
    r = norm.rvs(size=100)
    print(r)
    print(r.mean(), r.std(), r.var())
    fig, ax = plt.subplots(1, 1)
    mean, var, skew, kurt = norm.stats(moments='mvsk')
    x = np.linspace(norm.ppf(0.01),
                    norm.ppf(0.99), 100)

    ax.plot(x, norm.pdf(x),
            'r-', lw=5, alpha=0.6, label='norm pdf')
    #
    # ax.plot(x, norm.pdf(x),
    #        'r-', lw=5, alpha=0.6, label='norm pdf')
    vals = norm.ppf([0.001, 0.5, 0.999])
    np.allclose([0.001, 0.5, 0.999], norm.cdf(vals))
    r = norm.rvs(size=200)

    ax.hist(r, density=True, bins='auto', histtype='stepfilled', alpha=0.2)
    ax.set_xlim([x[0], x[-1]])
    ax.legend(loc='best', frameon=False)


def data(loc=10, scale=4, nums=100):
    x = np.linspace(norm.ppf(0.01, loc=loc, scale=scale), norm.ppf(0.99, loc=loc, scale=scale), nums)

    y = norm.pdf(x, loc=loc, scale=scale)
    return x, y


"""
麦克斯韦玻尔兹曼分布是正态分布在物理上的体现,
先有数据
检测正态性；为什么说它符合正态分布；
应用正态分布的性质(如果符合正态分布，就可以应用正态分布的性能)：
1、统计量
2、各种函数
"""

if __name__ == "__main__":
    # r = norm.rvs(size=100)
    x, y = data(loc=-4, scale=0.5)
    x2, y2 = data(loc=0, scale=1.5)
    x3, y3 = data(loc=10, scale=2.1)

    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, 'b-', lw=3, alpha=0.6, label='x1 pdf')
    ax.plot(x2, y2, 'r-', lw=3, alpha=0.6, label='x2 pdf')
    ax.plot(x3, y3, 'g-', lw=3, alpha=0.6, label='x3 pdf')
    ax.set_xlim(-6, 16)
    ax.set_ylim(0, 1)
    ax.legend(loc='best', frameon=False)

    plt.show()

    # norm_test()
    # norm_2()
    # plt.show()
