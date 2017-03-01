# -*- coding:utf8 -*-
from setuptools import setup, find_packages

setup(
    name="mytest",
    version="0.10",
    description="test module",
    author="jack cong",
    url="http://www.livedrof.com",
    license="LGPL",
    packages=find_packages(),
    scripts=["mytest/test.py"],
    py_modules=['mytest']
)
