'''
查找教师信息
'''
import prettytable as pt
import os,time
from database import Search_All, Search_Info
keytosqlcolumn={    #条件搜索信息类型转换成SQL列名
    '工号':'ID',
    '姓名':'Name',
    '年龄':'Age',
    '职称':'Title',
    '系名':'Department',
    '主授课程':'Course',
    '手机号码':'Phone_Number',
    '联系地址':'Address',}

def Search_Menu():  #查找功能主菜单
    table=pt.PrettyTable()
    table.field_names=['选项编号','选项']
    table.add_row(['1','显示所有教师信息'])
    table.add_row(['2','条件搜索教师信息'])
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

def Search_Main():  #条件搜索选项
    while True:
        os.system('cls')
        print('请输入一项搜索的信息类型及内容，以空格分隔，如:"电话号码 123"')
        print('可选数据类型: 工号,姓名,年龄,职称,系名,主授课程,手机号码,联系地址')
        key,value=input('请输入要搜索的信息: ').split()
        if(key in keytosqlcolumn):
            key=keytosqlcolumn[key]
            Search_Info(key,value)
            break
        else:
            print('信息类型错误，请检查后重试')
            time.sleep(1)

if __name__=='__main__':    #调试用
    Search_Menu()
