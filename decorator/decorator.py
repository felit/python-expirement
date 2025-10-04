#-*- coding:utf8 -*-
def foo():
    print("foo")


print(foo())
foo = lambda x: x + 1
print(foo(2))
def w1(func=None,hello="world"):
    print("添加装饰器:%s%s"%(func,hello))
    def inner(*args,**kwargs):
        print("from w1")
        var = 900
        return func(*args,**kwargs)
    return inner

@w1
def f1():
    print("f1")
"""
 f1 = def inner(*args,**kwargs):
        print "from w1"
        return _f1(*args,**kwargs)
"""


# @w1(hello="hello")
def f2():
    print("f2")
    # print var


def f3():
    print("f3")


def f4():
    print("f4")


print(f1)
f1()
f2()
f3()
f4()