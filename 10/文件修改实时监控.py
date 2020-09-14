content_old=[]
filename='10/test.txt'
while True:
    with open(filename) as f_obj:
        content=f_obj.read()
        if content != content_old:
            print(content)
            content_old=content