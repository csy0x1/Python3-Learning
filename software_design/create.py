'''
录入教师信息
'''

import prettytable,os
from database import Connect_DB

def Input_Info():
    os.system('cls')
    Teacher={}
    Teacher['ID']=input('请输入你的ID: ')
    Teacher['姓名']=input('请输入你的姓名: ')
    Teacher['年龄']=input('请输入你的年龄: ')
    Teacher['职称']=input('请输入你的职称: ')
    Teacher['系名']=input('请输入你所在系: ')
    Teacher['主授课程']=input('请输入你主要教授的课程: ')
    Teacher['电话号码']=input('请输入你的电话号码: ')
    Teacher['联系地址']=input('请输入你的联系地址: ')
    Show_Info(Teacher)



def Show_Info(info):
    os.system('cls')
    table=prettytable.PrettyTable()
    table.field_names=['信息','内容']
    for key,value in info.items():
        table.add_row([key,value])
    print(table.get_string(title='教师信息'))

Input_Info()