import sqlite3
import os
_cur = os.getcwd()
_dir = os.mkdir(_cur+'/database')
_dbasepath = _cur+'/database'
os.chdir(_dbasepath)

_path = os.getcwd()
conn = sqlite3.connect(_path + '/app')
c = conn.cursor()
c.execute("create table stocks (date text, trans text, symbol text,qty real, price real)")
c.execute("insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
c.close()

