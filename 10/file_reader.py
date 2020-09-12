with open('10\pi_digits.txt') as file_object: #相对路径
#with open('C:\Windows\System32\drivers\etc') as file_object: 绝对路径
    contents=file_object.read()
    print(contents)

#逐行读取
filename=input('please input file: ')  #可以实现拖动文件至终端窗口，自动获取路径读取, 路径不能带空格
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())