active=True
filename='10\ reason.txt'
while active:
    reason=input('Why you like programming? Type "quit" to quit ')
    if reason!='quit':
        with open(filename,'a') as file_object:
            file_object.write(reason+'\n')
    else:
        active=False
