'''
查找教师信息
'''
import prettytable as pt
from database import Search_All, Search_Info

def Search_Menu():  #查找功能主菜单
    table=pt.PrettyTable()
    table.field_names=['选项编号','选项']
    table.add_row(['1','显示所有教师信息'])
    table.add_row(['2','单独搜索教师信息'])
    print(table)
    Choose_Function()

def Choose_Function():  #用户选择所需功能，并跳转至相应界面
    Function={
        '1':Search_All,
        '2':Search_Main,
        'quit':exit,
    }
    choice=input('请选择功能，输入quit退出:')
    Function.get(choice,error)()

def error():  #默认选项
    print('选项错误')

def Search_Main():  #单独查找选项
    pass


