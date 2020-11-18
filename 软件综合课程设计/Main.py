#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   Main.py
@Time    :   2020-11-17 19:39:15
@Author  :   csy_x 
@Version :   2.0

教师管理系统主菜单
Todo:
1.增    create.py   11.17 updated
2.删    delete.py   11.17 updated
3.查    search.py   11.17 updated
4.改    modify.py   11.17 updated
5.权限系统*
6.开课系统    Create_Course.py    11.17 updated
7.工作量检索系统    @search.py    11.17 updated
8.教师ID自动分配*
'''
# Start


from Create_Course import Course_Menu
from modify import Modify_Info
from delete import Delete_Info
from create import Input_Info
from search import Search_Menu
import prettytable as pt

def Main_Menu():    #显示主菜单，提供选项信息
    table=pt.PrettyTable()  #创建选项表
    table.field_names=['选项编号','选项']
    table.add_row(['1','录入教师信息'])
    table.add_row(['2','修改教师信息'])
    table.add_row(['3','查询教师信息'])
    table.add_row(['4','删除教师信息'])
    table.add_row(['5','开设课程管理'])
    print(table)
    Choose_Function()

def Choose_Function():  #用户选择所需功能，并跳转至相应界面
    Function={
        '1':Input_Info,
        '2':Modify_Info,
        '3':Search_Menu,
        '4':Delete_Info,
        '5':Course_Menu,
        'quit':exit,
    }
    choice=input('请选择功能，输入quit退出:')
    Function.get(choice,error)()

def error():  #默认选项
    print('选项错误')
    return Main_Menu()

if __name__=='__main__':
    Main_Menu()
    