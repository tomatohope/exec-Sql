# -*- coding: UTF-8 -*-
#yum -y install python-devel mysql-devel  &&  pip install MySQL-python
import MySQLdb
from connectMysql import log

# execsql by sql
def execsql(host, port, user, passwd, database, sql, result):
    log.log("info", "database", database)
    log.log("info", "user", user)
    log.log("info", "host", host)
    log.log("info", "sql", sql)
    db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, database=database)
    cursor = db.cursor()
    cursor.execute(sql)
    results = []
    if str(result) == '1':
        results = cursor.fetchone()
    cursor.close()
    return results

# execsql by sqlfile
def execsqlfile(host, port, user, passwd, database, sqlfile, result):
    with open(sqlfile, 'r') as f:
        sql = f.read()
    results = execsql(host, port, user, passwd, database, sql, result)
    return results