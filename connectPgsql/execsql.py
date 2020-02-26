# coding: utf-8
import psycopg2
from connectPgsql import log
import json

# execsql by sql
def execsql(database, user, password, host, port, sql, result, dict):
    log.log("info", "database", database)
    log.log("info", "user", user)
    log.log("info", "host", host)

    dic = json.loads(dict)
    for key in dic:
        sql = sql.replace(key, dic[key])

    log.log("info", "sql", sql)
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql)
    results = []
    if str(result) == '1':
        results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

# execsql by sqlfile
def execsqlfile(database, user, password, host, port, sqlfile, result, dict):
    with open(sqlfile, 'r') as f:
        sql = f.read()
    results = execsql(database, user, password, host, port, sql, result, dict)
    return results
