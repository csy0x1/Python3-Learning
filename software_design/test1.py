def test1():
    print('im test1')
    return 3

def test2():
    while True:
        if(test1()==4):
            print('yup')
            break
        else:
            print('nupe')
            continue
    print('out of while')

test2()
