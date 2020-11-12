'''
负责控制数据库相关功能
'''

import sqlite3

def Connect_DB():
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    c=conn.cursor() #数据库指针

