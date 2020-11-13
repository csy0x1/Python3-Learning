'''
负责控制数据库相关功能
'''

import sqlite3
from sqlite3.dbapi2 import connect

def Insert_Info(dict):  #录入教师信息
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    c=conn.cursor() #数据库指针
    c.execute("insert into Teachers_info values(?,?,?,?,?,?,?,?)",[dict['ID'],dict['姓名'],dict['年龄'],dict['职称'],dict['系名'],dict['主授课程'],dict['电话号码'],dict['联系地址']])
    c.close()   #关闭数据库指针
    conn.commit()   #提交事务
    conn.close()    #关闭数据库连接