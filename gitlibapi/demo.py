# -*- coding:utf8 -*-
"""
https://blog.csdn.net/xie_0723/article/details/75215869
"""
import commands

import gitlab

url = 'https://code.vipkid.com.cn'
token = "K3g6x-ZgewGSX9Y-Xgnj"
gl = gitlab.Gitlab(url, token)
print gl
projects = gl.projects.list()
print projects
# 获取所有project的name,id
# for p in gl.projects.list(all=True, as_list=False):
for p in gl.projects.list():
    print(p.name, p.id)
# 获取公开的项目
projects = gl.projects.list(visibility='public', all=True)  # public, internal or private
for p in projects:
    print p.attributes['created_at'][:10], "\t", p.attributes['last_activity_at'][:10], "\t", p.attributes[
        'http_url_to_repo']
print(len(projects))


# print commands.getoutput("git clone https://code.vipkid.com.cn/commons/commons-metric")

class Project():
    """

    """

    # 分析项目中的pom文件 依赖关系，记录、groupId,artifactId,version(版本)，最后更新日期
    #     TODO 出错，报告错误
    #
    def __init__(self):
        self.https_repo = "https://code.vipkid.com.cn/commons/commons-metric.git"
        self.created_at = "2018-05-08"
        self.last_updated_at = "2018-05-11"

    def hello(self):
        pass