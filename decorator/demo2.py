# -*- coding:utf8 -*-
name = 'abc'
password = '123'


def certi(model):  # 装饰器
    def outr(fun):  # 装饰器加参数需要多加一层嵌套
        def login(*args, **kwargs):  # 为了兼容各类函数参数，添加 *args,**kwargs 不固定参数
            if model == 'password':
                print('enter password')
                user_name = raw_input('user_name ').strip()
                paswd = raw_input('password ').strip()
                if user_name == name and paswd == password:
                    print('pass')
                    return fun(*args, **kwargs)
                else:
                    print('error ')
                    exit()
            elif model == 'lamp':
                print('this is lamp')
                return fun(*args, **kwargs)
            else:
                print('error')

        return login

    return outr


def indxe():
    print('home page !!')


@certi(model='password')
def user():
    print('user page !!')


@certi(model='lamp')
def bbs(name):
    print('bbs %s!!' % name)


if __name__ == '__main__':
    indxe()
    user()
    bbs(name='yjj')
