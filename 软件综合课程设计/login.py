'''
登录功能
'''

from database import Connect_DB as Connect

def login():
    username=input('Please input your ID: ')
    password=input('Please input your password: ')
    sqlcom="select ID, Password from Account where ID=%s"%(username)    #通过用户名检索用户信息
    login_info=Connect.c.execute(sqlcom)    #执行SQL语句
    for info in login_info:     #登录验证
        uname=info[0]
        pwd=info[1]
        if uname==username and pwd==password:
            return True
        else:
            return False
