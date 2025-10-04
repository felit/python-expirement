import MySQLdb

db = MySQLdb.connect(host='54.222.199.188', port=3303, user='vipkid', passwd='Vi1pkidDb_rootZAQ!', db='vipkid')
cursor = db.cursor()
cursor.execute('show databases')
res = cursor.fetchall()
# print res
system_tables = ['information_schema', 'mysql', 'test']
# print list(res)
for tbl,  in list(res):
    cursor.execute('use %s' % tbl)
    cursor.execute('show tables')
    tables = cursor.fetchall()
    # print tbl
    # print tables
    for t,  in list(tables):
        print("%s\t%s" % (tbl,t))
