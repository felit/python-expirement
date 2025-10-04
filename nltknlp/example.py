content = """
岗位职责：

1、参与公司产品研发，完成开发任务，并对负责开发的模块进行测试、维护；
2、按规范编写相关技术文档；
3、与团队成员合作、沟通，对开发过程中问题进行总结；
4、负责系统需求分析和规划系统功能和接口；
5、参与产品的需求分析与讨论，完成部分功能设计，制定开发计划；
6、参与产品的技术支持工作；

岗位要求：

1、本科以上学历，3年及以上JAVA及Web项目开发经验；
2、熟悉J2EE规范，熟悉常用的数据结构，算法和设计模式；
3、熟悉主流JavaWeb框架，熟练使用JSP、Jquery、Bootstrap、H5等WEB开发基础技术；熟练使用Spring，SpringMVC,SpringCloud，SpringBoot，Mybatis等；
4、熟练使用Oracle或Mysql，拥有较好的数据库开发及设计能力；掌握Redis、MQ、ES等技术技术者优先；
5、有Hbase、Hive、Impala等Nosql经验者优先考虑；
6、熟练使用常见开发工具及技术Maven,Junit；
7、了解高并发和大数据相关知识者优先；
8、熟悉Linux常用命令；
9、熟练使用Github，SVN版本控制工具;
10、有良好的沟通表达能力，有大型互联网经验者优先。
"""

import nltk
from nltk.book import *
from nltk.util import bigrams

#先分词


# 单词搜索
print('单词搜索')
text1.concordance('boy')
text2.concordance('friends')

# 相似词搜索
print('相似词搜索')
text3.similar('time')