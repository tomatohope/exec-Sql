# coding: utf-8
from connectPgsql import execsql
execsql.execsql("dev_jing_dw", "postgres", "postgres", "192.168.43.63", "5432", "SELECT * from dev_jms_dw.test", "1")

