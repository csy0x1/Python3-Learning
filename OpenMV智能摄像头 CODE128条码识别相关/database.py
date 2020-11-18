'''
数据库相关系统
'''

import sqlite3,os

filename='F:/test/result.txt'

def removefile():   #移除文件
    if os.path.exists(filename):
        os.remove(filename)
    else:
        pass

def Connect_DB():   #连接数据库
    conn=sqlite3.connect('C://Users//Desktop-P21//codeDB.db') #连接到数据库
    c=conn.cursor()
    return conn,c

def commit(sqlcom):     #执行SQL命令
    conn,c=Connect_DB()
    c.execute(sqlcom)
    conn.commit()
    c.close()
    conn.close()

def duplicated(eamount,date,eid,content):   #重复数据处理
    sqlcom="update code set amount=%s,DATE='%s' where ID='%s'"%(eamount,date,eid)
    commit(sqlcom)
    sqlcom="update code set VALUE = '%s' where ID=0"%(content)  #SQL指令
    commit(sqlcom)
    removefile()

def Check_Last():   #检查上一次运行结束后的结果
    conn,c=Connect_DB()
    cursor = c.execute("SELECT amount,value from CODE where ID=0") #链接数据库，获取最新的ID编号
    amount=0    #数量
    iid=0       #数据库ID编号

    for row in cursor:  #读取最后一次存入数据库的内容
        cid=row[0]  #cid=下一个可用的ID号
        temp=row[1] #temp=最后一次存入的内容
    return filename,cid,temp

def New(cid,content,date):  #新数据处理
    sqlcom="INSERT INTO CODE(ID,VALUE,AMOUNT,DATE) VALUES('%s','%s',1,'%s')"%(cid,content,date) #SQL指令
    commit(sqlcom)
    cid+=1  #编号+1
    sqlcom="update code set value = '%s',amount=%s where ID=0"%(content,cid)  #SQL指令
    commit(sqlcom)
    removefile()
    return cid