# -*- coding: utf-8 -*-

def decrator(c=0, *dargs, **dkargs):
    print(dargs.__class__, dkargs.__class__)

    def wrapper(func):
        def _wrapper(*args, **kargs):
            print "decrator param:", dargs, dkargs
            print "function param:", args, kargs
            return func(*args, **kargs)

        return _wrapper

    return wrapper


@decrator(1, a=2)
def foo(x, y=0):
    print "foo", x, y


@decrator(5, 6, a=2)
def foo2():
    print("hello")


if __name__ == '__main__':
    foo(3, 4)
    print("\n")
    foo2()

'''
执行结果
decrator param: (1,) {'a': 2}
function param: (3, 4) {}
foo 3 4
[Finished in 0.1s]
'''
