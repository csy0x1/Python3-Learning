'''
查重系统
'''
import sqlite3

def CheckDuplicate(content):    #查重
    conn=sqlite3.connect('C://Users//Desktop-P21//codeDB.db') #连接到数据库
    c=conn.cursor()
    sqlcom="select * from code where value='%s' AND ID!=0"%(content)
    items = c.execute(sqlcom)
    for item in items:
        eid=item[0]      #获取已存在内容的ID
        evalue=item[1]   #将已在数据库中的内容赋值给变量evalue
        eamount=item[2] #获取已存在内容的数量
        if content==evalue:
            return eid,eamount
        else:
            return False