import jieba

words = jieba.cut("本文从多个角度分析了如何在Python中安装jieba库，包括使用pip、conda和手动安装等方法。同时，本文也简要介绍了如何使用jieba库进行中文分词。相信通过本文的学习，你已经学会了如何在Python中安装jieba库，并可以灵活地使用它进行中文分词。")
print("/".join(words))
