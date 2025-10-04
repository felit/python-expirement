import math

# iris数据集——决策树: https://blog.csdn.net/weixin_50197893/article/details/121714502
from sklearn import datasets

iris = datasets.load_iris()
print('iris.data的形状为(150,4)', iris.data.shape)
print('iris.data的特征名称为：', iris.feature_names)
print('iris.target的内容为：\n', iris.target)
print('iris.target的形状为', iris.target.shape)
print('iris.target的鸢尾花名称为', iris.target_names)


def compute(data):
    hh = h(data.target)


def ph(tuple_l):
    """
    条件信息熵
    :param tuple_l:
    :return:
    """
    amap = {}
    # 频率统计
    for a, y in tuple_l:
        if a not in amap:
            amap[a] = []
        amap[a].append(y)

    ll = len(tuple_l)
    hh = 0
    # 计算熵
    for a, val_list in amap.items():
        hh += len(val_list) / ll * h(val_list)
    print(hh)
    return hh


def h(l):
    """
    计算信息熵
    :param l:
    :return:
    """
    map = {}
    # 频率统计
    for val in l:
        if val not in map:
            map[val] = 0
        map[val] += 1
    ll = len(l)
    h = 0
    # 计算熵
    for k, count in map.items():
        print(k, count / ll, math.log2(count / ll), count / ll * math.log2(count / ll))
        h -= count / ll * math.log2(count / ll)
    print(h)
    return h


compute(iris)
print("len(iris.feature_names)", iris.data.shape[1])
result = []
for ai in range(0, iris.data.shape[1]):
    data = [(a[ai], y) for a, y in zip(iris.data, iris.target)]
    result.append((iris.feature_names[ai], ph(data)))
    # [('sepal length (cm)', 0.7080248798300983), ('sepal width (cm)', 1.0683196250406586), ('petal length (cm)', 0.1386459770753561), ('petal width (cm)', 0.14906466204571436)]
result.sort(key=lambda x: x[1])
# [('petal length (cm)', 0.1386459770753561), ('petal width (cm)', 0.14906466204571436), ('sepal length (cm)', 0.7080248798300983), ('sepal width (cm)', 1.0683196250406586)]
print(result)
