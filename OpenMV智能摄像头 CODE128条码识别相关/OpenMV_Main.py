#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   OpenMv_Main.py
@Time    :   2020/11/17 15:28:12
@Author  :   csy_x 
@Version :   2.0
2020/11/7  程序编写完成
2020/11/17 重构代码
'''
# Start

import datetime,time,os
from CheckDuplicate import CheckDuplicate
from database import duplicated,Check_Last,New

filename,cid,temp=Check_Last()
#cid为最小可用的ID，temp为最后一次存入的内容,eid为重复内容所在的ID,eamount为重复内容数量
while True:
    try:
        date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename) as f:
            #date="%s/%s/%s %s-%s-%s"%(i.year,i.month,i.day,i.hour,i.minute,i.second) #获取当前时间
            content=f.read()
        #if content!=temp:
        if(CheckDuplicate(content)):   #数据库中存在此内容
            eid,eamount=CheckDuplicate(content)
            print("duplicated")
            eamount+=1
            duplicated(eamount,date,eid,content)
        else:
            print(content)
            cid=New(cid,content,date)
        time.sleep(1)
    except (FileNotFoundError,OSError):
        pass

