__author__ = 'congsl'
import datetime
print datetime.date(2009, 10, 17).__class__
print datetime.datetime.strptime('%s'%datetime.date(2009, 10, 17),'%Y-%m-%d')
print datetime.datetime.strptime('%s'%datetime.date(2009, 10, 17),'%Y-%m-%d').__class__
