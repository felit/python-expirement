# -*- coding:utf8 -*-
import matplotlib as mpl

print mpl.rcParams
print len(mpl.rcParams)
mpl.rc('lines', linewidth=2, color='r')
print mpl.get_configdir()