'''
教师管理系统主菜单
Todo:
1.增
2.删
3.查 (WIP)
4.改
'''

import prettytable as pt
from create import Create

def Main_Menu():    #显示主菜单，提供选项信息
    table=pt.PrettyTable()  #创建选项表
    table.field_names=['选项编号','选项']
    table.add_row(['1','录入教师信息'])
    table.add_row(['2','修改教师信息'])
    table.add_row(['3','查询教师信息'])
    table.add_row(['4','删除教师信息'])
    print(table)

def Choose_Function():  #用户选择所需功能，并跳转至相应界面
    Function={
        '1':Create,
        'quit':exit,
    }
    choice=input('请选择功能，输入quit退出:')
    Function.get(choice,error)()

def error():  #默认选项
    print('选项错误')

Main_Menu()
Choose_Function()