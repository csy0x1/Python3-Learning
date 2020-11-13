'''
删除教师信息
'''
from database import Delete, Search_Info
import os

def Delete_Info():
    os.system('cls')
    print('删除信息仅支持通过工号删除，一旦删除将无法恢复，请谨慎操作')
    tid=input('请输入要删除的工号: ')
    Search_Info('ID',tid)
    print("请仔细核对将删除的教师，输入 Confirm Delete ID %s 以继续"%(tid))
    confirm=input()
    if((confirm=='Confirm Delete ID %s'%(tid))):
        Delete(tid)
        print('删除成功!')
    else:
        print('删除失败!')

if __name__=='__main__':    #调试用
    Delete_Info()