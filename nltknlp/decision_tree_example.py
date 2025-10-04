from sklearn import tree
from sklearn import datasets

iris = datasets.load_iris()
x = iris.data  # 数据特征
y = iris.target  # 数据特征
# 评价标准为 criterion='entropy',决策树最大深度为 max_depth=2
clf_tree=tree.DecisionTreeClassifier(criterion='entropy',max_depth=13)
clf_tree.fit(x,y)
dot_data=tree.export_graphviz(clf_tree,out_file=None,
                              feature_names=iris.feature_names,
                              class_names=True,filled=True,rounded=True)
print('dot_data决策结果数据文件为:\n',dot_data)
from IPython.display import Image
# from IPython import  display
import pydotplus
graph = pydotplus.graph_from_dot_data(dot_data)
img = Image(graph.create_png())
graph.write_png("iris.png")
# display.display(img)

# graph.write_pdf("iris.pdf")