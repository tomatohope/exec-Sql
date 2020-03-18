# coding: utf-8
import psycopg2, sys, datetime

"""
优化 analystic db posql 某个数据库下的 所有表空间
vacuum [tablename]

优化 analystic db posql 某个数据库下的 所有表执行代价
analyze [tablename]

useage:
python pgsql_vacuum_optimize_table.py '[database]' '[superuser]' '[superpassword]' '[host]' '[port]' '[schemaname]'
"""

def execsql(database, user, password, host, port, sql, result):
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

def pgsql_optimize(database, superuser, superpassword, host, port, schemaname, sql):
    gettablesql = "SELECT  tablename   FROM   pg_tables WHERE schemaname = " + "\'" + schemaname + "\'"
    tables = execsql(database, superuser, superpassword, host, port, gettablesql, 1)
    print("tables_num: ", len((tables)))

    modulesql = sql + schemaname + "."
    sta_time = datetime.datetime.now()
    for i in range(len(tables)):
        sql = modulesql + tables[i][0]
        print("sql       : ", sql)
        start_time = datetime.datetime.now()
        execsql(database, superuser, superpassword, host, port, sql, 0)
        end_time = datetime.datetime.now()
        token_time = (end_time - start_time).total_seconds()
        print("start time: ", start_time.replace(microsecond=0), "sqlnum", i, sql)
        print("token time: ", token_time, "s.", "         sqlnum", i, sql)
        print("end   time: ", end_time.replace(microsecond=0), "sqlnum", i, sql)
        print("\n")

    end_time = datetime.datetime.now()
    duration_time = (end_time - sta_time).total_seconds()
    print("action    :", modulesql, "*")
    print("token_time:", duration_time, "s")
    print("start_time:", sta_time.replace(microsecond=0))
    print("end_time  :", end_time.replace(microsecond=0), "\n")

############################################
database = sys.argv[1]
superuser = sys.argv[2]
superpassword = sys.argv[3]
host = sys.argv[4]
port = sys.argv[5]
schemaname = sys.argv[6]

sta_time = datetime.datetime.now()
# vacuum
pgsql_optimize(database, superuser, superpassword, host, port, schemaname, "vacuum ")

# analyze
pgsql_optimize(database, superuser, superpassword, host, port, schemaname, "analyze ")

end_time = datetime.datetime.now()
duration_time = (end_time - sta_time).total_seconds()
print("action    : TotalexecTime")
print("token_time:", duration_time, "s")
print("start_time:", sta_time.replace(microsecond=0))
print("end_time  :", end_time.replace(microsecond=0))