'''
负责控制数据库相关功能
Todo:
1.返回操作是否成功的提示
'''

import sqlite3,prettytable
from sqlite3.dbapi2 import IntegrityError, InternalError, connect
from prettytable import from_db_cursor

def Insert_Info(dict):  #录入教师信息
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    c=conn.cursor() #数据库指针
    c.execute("insert into Teachers_info values(?,?,?,?,?,?,?,?,0)",[dict['工号'],dict['姓名'],dict['年龄'],dict['职称'],dict['系名'],dict['主授课程'],dict['手机号码'],dict['联系地址']])
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
        c.close()
        conn.close()
        return False
    else:
        c.close()
        conn.close()
        return table

def Search_All():   #显示全部信息
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    c=conn.cursor() #数据库指针
    info = c.execute("select * from Teachers_info")
    table=from_db_cursor(info)
    print(table.get_string(title='全部教师信息'))
    c.close()
    conn.close()

def Delete(tid):    #删除教师信息
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    c=conn.cursor() #数据库指针
    c.execute("delete from Teachers_info where ID=%s"%(tid)) #删除工号为tid的记录
    conn.commit()
    c.close()
    conn.close()

def Modify(key,value,tid):    #修改教师信息
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    c=conn.cursor() #数据库指针
    c.execute("update Teachers_info set %s='%s' where ID=%s"%(key,value,tid))
    conn.commit()
    c.close()
    conn.close()

def Search_Course(): #查看课程
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    c=conn.cursor() #数据库指针
    info=c.execute("select * from Course_info")
    table=from_db_cursor(info)
    print(table.get_string(title='全部课程信息'))
    c.close()
    conn.close()

def Insert_Course(course): #开设课程
    conn=sqlite3.connect('C://Users//Desktop-P21//TeachersDB.db')   #连接到数据库
    conn.execute("PRAGMA foreign_keys = 1")
    c=conn.cursor() #数据库指针
    try:
        c.execute("insert into Course_info values(?,?,?,?)",[course['课程编号'],course['课程名称'],course['课程学时'],course['教师工号']])
        c.execute("UPDATE Teachers_info SET Total_Course_Hour=Total_Course_Hour+%s WHERE id=%s"%(course['课程学时'],course['教师工号']))
        conn.commit()
        c.close()
        conn.close()
        return 1
    except(sqlite3.IntegrityError):
        return False

