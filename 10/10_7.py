while True:
    try:
        number1=input('please input a number: ')
        number2=input('please input a number: ')
        result=int(number1)+int(number2)
    except ValueError:
        print('\nYou can only input a number\n')
    else:
        print(result)