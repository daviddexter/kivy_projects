import sqlite3
import os
from base import Base

class dbAccess:
    def __init__(self,_folder):
        self._folder = _folder
        base = Base(self._folder)
        if base.checker() == True:
            self.createDb()
        else:
            self.accessDb()

    def createDb(self):
        #print('created database')
        _cur = os.getcwd()
        conn = sqlite3.connect(_cur + '/list')
        c = conn.cursor()
        c.execute('create table mylist (listid interger, title text, body text, date text)')
        conn.commit()


    def accessDb(self):
        #print('accessed database')
        _cur = os.getcwd()
        conn = sqlite3.connect(_cur + '/list')
        c = conn.cursor()
        c.execute("""insert into mylist (listid , title, body, date ) values (2,'title','body','date')""")
        c.execute('select * from mylist order by listid desc')
        num = c.fetchall()
        #print(num)
        if num == []:
            return False
        else:
            for row in num:
                return row









