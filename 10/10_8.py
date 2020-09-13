def readfile():
    filenames=['10\cats.txt','10\dogs.txt']
    for filename in filenames:
        with open(filename) as file_object:
            content=file_object.read()
            print(content.rstrip())
        print('\n')
try:
    readfile()
except FileNotFoundError:
    #print('File not found')  #10_8
    pass  #10_9