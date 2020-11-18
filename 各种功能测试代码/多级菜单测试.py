def Choose_Function():  #用户选择所需功能，并跳转至相应界面
    Function={
        '1':test1,
        'quit':exit,
    }
    choice=input('请选择功能，输入quit退出:')
    Function.get(choice,error)()

def error():
    print('error')

def test1():
    while True:
        try:
            print('hi')
        except(KeyboardInterrupt):
            return Choose_Function()

Choose_Function()
print('main')
