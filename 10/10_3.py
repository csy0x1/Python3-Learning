name=input('Please input your name: ')
filename='10\guest.txt'
with open(filename,'a') as file_object:
    file_object.write(name+'\n')
