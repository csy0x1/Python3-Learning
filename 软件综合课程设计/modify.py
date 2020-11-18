'''
修改教师信息
'''

import os,time
from database import Modify, Search_Info
from search import keytosqlcolumn

def Modify_Main(tid):  #修改信息
    if(Search_Info('ID',tid)):
        table=Search_Info('ID',tid)
        while True:
            os.system('cls')
            print(table.get_string(title='查询结果'))
            print('请输入一项要修改的信息类型及内容，以空格分隔，如:"手机号码 123"')
            print('可选数据类型: 工号,姓名,年龄,职称,系名,主授课程,手机号码,联系地址')
            try:
                key,value=input('请输入要修改的信息: ').split()
            except(ValueError):
                print('输入错误，请检查后再试')
                time.sleep(1)
                continue
            if(key in keytosqlcolumn):
                key=keytosqlcolumn[key]
                Search_Info('ID',tid)
                result=Modify(key,value,tid)
                if(result==False):
                    print('操作失败，请检查后重试!')
                    break
                else:
                    print('操作成功！')
                    break
            else:
                print('信息类型错误，请检查后重试')
                time.sleep(1)
    else:
        print('\n暂无相关信息')
        time.sleep(1)
    return Modify_Info()


def Modify_Info():  #查询信息
    os.system('cls')
    print('仅支持通过工号查询')
    tid=input('请输入要修改教师信息的工号: ')
    Modify_Main(tid)

if __name__=='__main__':
    Modify_Info()
