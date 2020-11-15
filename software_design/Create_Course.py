'''
开课系统
Todo:
1.至少可以定义课程编号，课程名称，开课学时数，授课教师
2.授课教师自动同步至教师信息主要教授课程(开课多门时主授课程判定方式有疑虑，非必要，待考虑)
'''

from database import Insert_Course, Search_Course
import prettytable,os,time


def Course_Menu():  #主菜单
    os.system('cls')
    menu=prettytable.PrettyTable()
    menu.field_names=(['选项编号','选项'])
    menu.add_row(['1','查看当前所有课程'])
    menu.add_row(['2','开设一门新的课程'])
    print(menu.get_string(title='课程选项'))
    Choose_Function()

def Choose_Function():  #选择功能
    Function={
        '1':Search_Course,
        '2':Create_Course,
        'quit':exit,
    }
    choice=input('请选择功能，输入quit退出: ')
    Function.get(choice,error)()

def error():    #默认选项
    print('选项错误')

def Create_Course():    #开设新课程
    flag=True   #循环标识符
    os.system('cls')
    course={}
    course['课程编号']=input('请输入课程编号: ')
    course['课程名称']=input('请输入课程名称: ')
    course['课程学时']=input('请输入课程学时: ')
    course['教师工号']=input('请输入授课教师工号: ')
    while flag:
        Show_Info(course)
        info=input('请输入要修改的信息名以及内容，一次一条，以空格分隔(如课程编号 XX): ')
        if(info==''):   #检测用户提交
            if(Insert_Course(course)==1):
                print('操作成功！')            
                flag=False
                break
            else:
                print('操作失败，请检查信息是否输入正确')
                print('确保工号输入正确，课程编号无重复')
                time.sleep(1)
                continue
        index=0
        for i in info:  #获取用户输入的key值和value值
            if i==' ':
                break
            else:
                index+=1
        key=info[0:index]
        value=info[index+1:]    
        if(key in course):     #检测用户输入的key值是否存在
            course[key]=value
        else:
            print('键值不存在!')
            time.sleep(1)


def Show_Info(info):    #显示课程信息
    os.system('cls')
    table=prettytable.PrettyTable()     #创建表格
    table.field_names=['信息','内容']   #设置表头
    for key,value in info.items():
        table.add_row([key,value])
    print(table.get_string(title='课程信息'))


if __name__ == '__main__':
    Course_Menu()
    Choose_Function()
