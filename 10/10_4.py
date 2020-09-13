active=True 
filename='10\guest_book.txt'
while active:
    name=input('Please input your name, type "quit" to quit: ')
    if name != 'quit':
        with open(filename,'a') as file_object:
            file_object.write(name.title()+'\n')
        print('Hello! '+name)
    else:
        active=False