# coding: utf-8
import psycopg2, sys

"""
GRANT owner ON ALL TABLES IN SCHEMA on database TO a account
useage:
python updatePgsqlOwner.py database user password host port schemaname account
"""

def execsql(database, user, password, host, port, sql,result):
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

############################################
database = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
host = sys.argv[4]
port = sys.argv[5]
schemaname = sys.argv[6]
account = sys.argv[7]

sql = "SELECT  tablename   FROM   pg_tables WHERE schemaname = " + "\'" + schemaname + "\'"
tables = execsql(database, user, password, host, port, sql, 1)
print("tables:", tables)

for i in range(len(tables)):
    sql = 'alter table ' + schemaname + '.' + tables[i][0] + ' owner to ' + account + ';'
    print("sql", i, sql + '\n')
    execsql(database, user, password, host, port, sql, 0)