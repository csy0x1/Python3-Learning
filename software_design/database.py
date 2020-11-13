'''
负责控制数据库相关功能
'''

import sqlite3,prettytable
from sqlite3.dbapi2 import connect

from prettytable import from_db_cursor

def Insert_Info(dict):  #录入教师信息
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    c=conn.cursor() #数据库指针
    c.execute("insert into Teachers_info values(?,?,?,?,?,?,?,?)",[dict['ID'],dict['姓名'],dict['年龄'],dict['职称'],dict['系名'],dict['主授课程'],dict['电话号码'],dict['联系地址']])
    c.close()   #关闭数据库指针
    conn.commit()   #提交事务
    conn.close()    #关闭数据库连接

def Search_Info(key,value):     #条件搜索信息
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    c=conn.cursor() #数据库指针
    '''
    模糊搜索尝试
    if(Fuzzy=='Y'):
        value='%'+value+'%'
        info=c.execute("select * from Teachers_info where %s Like '%s'"%(key,value))
    else:
    '''
    info=c.execute("select * from Teachers_info where %s='%s'"%(key,value))
    table=from_db_cursor(info)  
    if(len(list(table))==0):    #若查询不到信息，返回的表长为0
        print('查找不到相关信息!')
    else:
        print(table.get_string(title='查询结果'))
    c.close()
    conn.close()

def Search_All():   #显示全部信息
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    c=conn.cursor() #数据库指针
    info = c.execute("select * from Teachers_info")
    table=from_db_cursor(info)
    print(table.get_string(title='全部教师信息'))
    c.close()
    conn.close()

def Delete(tid):
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    c=conn.cursor() #数据库指针
    c.execute("delete from Teachers_info where ID=%s"%(tid)) #删除工号为tid的记录
    conn.commit()
    c.close()
    conn.close()
