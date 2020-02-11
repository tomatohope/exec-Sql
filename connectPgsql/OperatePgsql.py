# coding: utf-8
from connectPgsql import execsql
import sys

database = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
host = sys.argv[4]
port = sys.argv[5]
sqlfile = sys.argv[6]

execsql.execsqlfile(database, user, password, host, port, sqlfile, "0")
