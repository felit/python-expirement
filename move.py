# -*- coding:utf8 -*-
import psycopg2
from pymongo import *
import datetime

client = MongoClient('localhost', 27017)
mongodb = client.trade
membership_coll = mongodb.membership
conn = psycopg2.connect(host='192.168.248.11',
                        port=5432,
                        database='crm',
                        user='trace',
                        password='readonly')
cursor = conn.cursor()

sql = """
    select id,gender,"name",mobile,''||birthday,merchant_id,brand_id, constellation,''||join_date
    from trade.membership
    where id >= %s and id < %s
    LIMIT %s
"""
max_id = 51195387
tmp_id = 0
num = 10000
while (tmp_id < max_id):
    s = sql % (tmp_id, tmp_id + num, num)
    cursor.execute(s)
    res = cursor.fetchall()
    tmp_id += num
    join_date = None
    birthday = None
    try:
        pass
    except Exception, e:
        pass
    membership_coll.insert_many([
        {
            'id': row[0],
            'gender': row[1],
            'name': row[2],
            'mobile': row[3],
            'birthday': row[4] and datetime.datetime.strptime('%s' % row[4], '%Y-%m-%d'),
            'merchant_id': row[5],
            'brand_id': row[6],
            'constellation': row[7],
            'join_date': row[8] and datetime.datetime.strptime('%s' % row[8], '%Y-%m-%d'),
        } for row in res])
