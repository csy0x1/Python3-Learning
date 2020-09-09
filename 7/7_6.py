age=''
active='true'
while active == 'true':
    age=input('age? Type"quit" to exit ')
    if age == 'quit':
        active='false'
        break
    else:
        age=int(age)
        if age < 3:
            print('free')
        elif age >=3 and age < 12:
            print('$10')
        else:
            print('$15')
