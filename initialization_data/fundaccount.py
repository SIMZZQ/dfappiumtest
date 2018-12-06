# coding:utf-8
import cx_Oracle

username = 'hs_acct'
userpsw = 'hundsun'
host = '172.16.45.37'
port = 1521
dbname = 'CFGL44'
dsn = cx_Oracle.makedsn(host,port,dbname)
conn = cx_Oracle.connect(username,userpsw,dsn)
cursor = conn.cursor()
sql = 'select*from hs_acpt.regcustbond a where join_app_user_id = "95503700046108"'
cursor.execute(sql)
result = cursor.fetchall()
print(result)
cursor.close()
conn.close()