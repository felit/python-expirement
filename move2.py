# -*- coding:utf8 -*-
import psycopg2
from pymongo import *
import datetime

client = MongoClient('localhost', 27017)
mongodb = client.trade
membership_coll = mongodb.membership_stats
conn = psycopg2.connect(host='192.168.248.11',
                        port=5432,
                        database='crm',
                        user='trace',
                        password='readonly')
cursor = conn.cursor()

sql = """
        SELECT brand_id,
            membership_id,
            COUNT (DISTINCT trans_date) AS consume_date,
            (
                SUM (amount) / (COUNT(DISTINCT trans_date))
            ) :: INTEGER AS consume_amount,
            MAX (trans_date) max_trans_date
        FROM
            public.trans_water
        WHERE
            trans_date >= '2015-12-22'
        AND trans_date < '2016-12-22'
        AND trans_code IN (
            '0002',
            '2002',
            '1002',
            '3001'
        )
        AND reversedflag = 'f'
        AND revocationflag = 'f'
        GROUP BY
            brand_id,
            membership_id
"""
num = 10000
cursor.execute(sql)
print 'execute completely'
res = cursor.fetchmany(num)
while (len(res) > 0):
    membership_coll.insert_many([
        {
            'brand_id': row[0],
            'membership_id': row[1],
            'consume_date': row[2],
            'consume_amount': row[3],
            'max_trans_date': row[4] and datetime.datetime.strptime('%s' % row[4], '%Y-%m-%d'),
        } for row in res])
    res = cursor.fetchmany(num)