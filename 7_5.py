#7_5
age=''
while True:
    age=input('age? ')
    age=int(age)
    if age < 3:
        print('free')
    elif age >=3 and age < 12:
        print('$10')
    else:
        print('$15')