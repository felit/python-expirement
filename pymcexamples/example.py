import pymc as pm

"""
==============================================================================================================================================================================================================================================
 Package                                                           架构                                              版本                                                            源                                                  大小
==============================================================================================================================================================================================================================================
正在安装:
 python3-devel                                                     x86_64                                            3.6.8-19.el7_9                                                  updates                                            217 k
为依赖而安装:
 dwz                                                               x86_64                                            0.11-3.el7                                                      base                                                99 k
 perl-srpm-macros                                                  noarch                                            1-8.el7                                                         base                                               4.6 k
 python-rpm-macros                                                 noarch                                            3-34.el7                                                        base                                               9.1 k
 python-srpm-macros                                                noarch                                            3-34.el7                                                        base                                               8.8 k
 python3-rpm-generators                                            noarch                                            6-2.el7                                                         base                                                20 k
 python3-rpm-macros                                                noarch                                            3-34.el7                                                        base                                               8.1 k
 redhat-rpm-config                                                 noarch                                            9.1.0-88.el7.centos                                             base                                                81 k
 zip                                                               x86_64                                            3.0-11.el7                                                      base                                               260 k
为依赖而更新:
 python3                                                           x86_64                                            3.6.8-19.el7_9                                                  updates                                             70 k
 python3-libs                                                      x86_64                                            3.6.8-19.el7_9                                                  updates                                            6.9 M

"""

"""

ImportError: cannot import name 'find_namespace_packages'
sudo pip3 install  -i https://pypi.douban.com/simple/  -U setuptools

***> libhdf5-serial-devel netcdf-bin libnetcdf-devel

onnx
MxNet


"""

"""
sudo pip3 install  -i https://pypi.douban.com/simple/  pymc

sudo yum install -y python3-devel
sudo yum install -y lapack-devel
"""


def ss():
    alpha = 2.0012
    lambda_ = pm.Exponential("poisson_param", 1)
    data_generator = pm.Poisson("data_generator", lambda_)
    data_plus_one = data_generator + 1
    print(data_plus_one)


def ss2():
    alpha = 2.344
    lambda_1 = pm.Exponential("lambda_1", alpha)
    lambda_2 = pm.Exponential("lambda_2", alpha)
    tau = pm.DiscreteUniform("tau", lower=0, upper=2)
    print("Random output:", tau.random(), tau.random(), tau.random())


ss2()
