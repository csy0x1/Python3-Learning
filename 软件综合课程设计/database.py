'''
负责控制数据库相关功能
Todo:
1.返回操作是否成功的提示    Done 11/17 updated
'''

import sqlite3,prettytable,time
from sqlite3.dbapi2 import IntegrityError, InternalError, connect
from prettytable import from_db_cursor

filename='C://Users//Desktop-P21//TeachersDB.db'    #数据库文件

def Insert_Info(dict):  #录入教师信息
    conn=sqlite3.connect(filename)   #连接到数据库
    c=conn.cursor() #数据库指针
    try:
        c.execute("insert into Teachers_info values(?,?,?,?,?,?,?,?,0)",[dict['工号'],dict['姓名'],dict['年龄'],dict['职称'],dict['系名'],"null",dict['手机号码'],dict['联系地址']])
        c.close()   #关闭数据库指针
        conn.commit()   #提交事务
        conn.close()    #关闭数据库连接
    except(sqlite3.Error):
        c.close()   #关闭数据库指针
        conn.close()    #关闭数据库连接
        return False

def Search_Info(key,value):     #条件搜索信息
    conn=sqlite3.connect(filename)   #连接到数据库
    c=conn.cursor() #数据库指针
    '''
    模糊搜索尝试
    if(Fuzzy=='Y'):
        value='%'+value+'%'
        info=c.execute("select * from Teachers_info where %s Like '%s'"%(key,value))
    else:
    '''
    info=c.execute("select ID as 工号, Name as 姓名, Age as 年龄, Title as 职称, Department as 系名, \
    Course as 主授课程, Phone_Number as 手机号码, Address as 联系地址, Total_Course_Hour as 总开课学时 from Teachers_info where %s='%s'"%(key,value))
    rows=c.fetchall()
    #table=from_db_cursor(info)  
    #if(len(list(table))==0):    #若查询不到信息，返回的表长为0
    if(len(rows)==0):
        print("\n目前暂无教师信息")
        c.close()
        conn.close()
        return False
    else:
        c.close()
        conn.close()
        return rows

def Search_All():   #显示全部信息
    conn=sqlite3.connect(filename)   #连接到数据库
    c=conn.cursor() #数据库指针
    try:
        info = c.execute("select ID as 工号, Name as 姓名, Age as 年龄, Title as 职称, Department as 系名, \
            Course as 主授课程, Phone_Number as 手机号码, Address as 联系地址, Total_Course_Hour as 总开课学时 from Teachers_info")
        rows=c.fetchall()
        #table=from_db_cursor(info)
        if(len(rows)==0):
            print("\n目前暂无教师信息")
            #time.sleep(1)
            return False
        else:
            #print(table.get_string(title='全部教师信息'))
            row=len(rows)
            #print(row)
            c.close()
            conn.close()
            return row,rows
    except(sqlite3.Error):
        c.close()
        conn.close()
        print('操作失败!')
        time.sleep(1)
        return False

def Delete(tid):    #删除教师信息
    conn=sqlite3.connect(filename)   #连接到数据库
    c=conn.cursor() #数据库指针
    try:
        c.execute("delete from Teachers_info where ID='%s'"%(tid)) #删除工号为tid的记录
        conn.commit()
        c.close()
        conn.close()
    except(sqlite3.Error):  #删除行数为0行(删除不存在的数据)时不报错
        c.close()
        conn.close()
        return False

def Modify(data):    #修改教师信息
    conn=sqlite3.connect(filename)   #连接到数据库
    c=conn.cursor() #数据库指针
    try:
    #c.execute("update Teachers_info set '%s'='%s' where ID='%s'"%(key,value,tid))
        c.execute("update Teachers_info set Name='%s',Age=%d,Title='%s',Department='%s',Phone_Number='%s'\
        ,Address='%s' where ID='%s'"%(data[1],int(data[2]),data[3],data[4],data[5],data[6],data[0]))
        conn.commit()
        c.close()
        conn.close()
        return True
    except(sqlite3.Error):
        test=sqlite3.Error.args[0]
        print(test)
        c.close()
        conn.close()
        return False

def Search_Course(): #查看课程
    conn=sqlite3.connect(filename)   #连接到数据库
    c=conn.cursor() #数据库指针
    try:
        info=c.execute("select ID as 课程编号,C_Name as 课程名称,Name as 姓名,C_Hour as 课程学时\
            from Teachers_info inner join course_info\
            On Teachers_info.ID=Course_info.T_ID\
            Union\
            select ID as 课程编号,C_Name as 课程名称,Name as 姓名,C_Hour as 课程学时\
            from Teachers_info left outer join course_info\
            On Teachers_info.ID=Course_info.T_ID")
        table=from_db_cursor(info)
        if(len(list(table))==0):
            print('\n暂无课程信息！')
            return False
        else:
            print(table.get_string(title='全部课程信息'))
            c.close()
            conn.close()
    except(sqlite3.Error):
        c.close()
        conn.close()
        print('操作失败!')
        time.sleep(1)
        return False
    '''
    应使用的SQL语句
    select ID as 工号,C_Name as 课程名称,Name as 姓名,C_Hour as 课程学时 from Teachers_info inner join course_info
        On Teachers_info.ID=Course_info.T_ID
    Union
        select ID as 工号,C_Name as 课程名称,Name as 姓名,C_Hour as 课程学时 from Teachers_info left outer join course_info
        On Teachers_info.ID=Course_info.T_ID
    '''

def Insert_Course(course): #开设课程
    conn=sqlite3.connect(filename)   #连接到数据库
    conn.execute("PRAGMA foreign_keys = 1")
    c=conn.cursor() #数据库指针
    c_name=''
    try:
        c.execute("insert into Course_info values(?,?,?,?)",[course['课程编号'],course['课程名称'],course['课程学时'],course['教师工号']])
        c.execute("UPDATE Teachers_info SET Total_Course_Hour=Total_Course_Hour+%s WHERE id='%s'"%(course['课程学时'],course['教师工号']))
        items=c.execute('select C_Name, max(C_Hour) from Course_info WHERE T_ID="%s"'%(course['教师工号']))
        for row in items:
            c_name=row[0]
        c.execute('update Teachers_info set Course="%s" where ID="%s"'%(c_name,course['教师工号']))     
        #138~141行为将Teachers_info表主授课程字段更新为该教师开课学时最长的课程
        conn.commit()
        c.close()
        conn.close()
        return 1
    except(sqlite3.Error):
        return False

def Search_Hour():  #工作量查询
    conn=sqlite3.connect(filename)   #连接到数据库
    c=conn.cursor() #数据库指针
    try:
        info=c.execute("select ID as 工号,Name as 姓名,Total_Course_Hour as 总开课学时\
            from Teachers_info inner join course_info\
            On Teachers_info.ID=Course_info.T_ID\
            Union\
            select ID as 工号,Name as 姓名,Total_Course_Hour as 总开课学时\
            from Teachers_info left outer join course_info\
            On Teachers_info.ID=Course_info.T_ID\
            ORDER by Total_Course_Hour DESC")
        table=from_db_cursor(info)
        if(len(list(table))==0):
            print('\n暂无工作量信息!')
        else:
            print(table.get_string(title='开课信息'))
            c.close()
            conn.close()
    except(sqlite3.Error):
        c.close()
        conn.close()
        print('操作失败!')
        time.sleep(1)
        return False

    '''
    应使用的SQL语句
    select ID as 工号,Name as 姓名,Total_Course_Hour as 总开课学时 from Teachers_info inner join course_info
            On Teachers_info.ID=Course_info.T_ID
        Union
            select ID as 工号,Name as 姓名,Total_Course_Hour as 总开课学时 from Teachers_info left outer join course_info
            On Teachers_info.ID=Course_info.T_ID
            ORDER by Total_Course_Hour DESC
    '''
