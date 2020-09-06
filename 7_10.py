result={}
active=True
while active:
    name=input('What is your name? ')
    place=input('Where do u want to go most ')
    result[name]=place
    temp=input('Continue? Y/N')
    if temp == 'N':
        active=False
print(result)
for name,place in result.items():
    print(name+' wants to go to '+place)
