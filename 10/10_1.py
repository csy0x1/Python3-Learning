filepath='10\learning_python.txt'
with open(filepath,encoding='utf-8') as filetest1:
    print('读取整个文件: ')
    content=filetest1.read()
    print(content.rstrip())

with open(filepath,encoding='utf-8') as filetest2:
    print('\n遍历文件对象: ')
    lines=filetest2.readlines() #注意是readline[s] 不是readline, 区别： https://blog.csdn.net/weixin_41656968/article/details/80205717
    for line in lines:
        print(line.strip())

with open(filepath,encoding='utf-8') as filetest3:
    lines=filetest3.readlines()

print('\nwith代码块外打印: ')
for line in lines:
    print(line.strip())

#10_2
with open(filepath,encoding='utf-8') as filetest4:
    lines=filetest4.readlines()

print('\n单词替换测试: ')
for line in lines:
    line.replace('Python','C++') #replace不会改变原字符串内容，此处替换不会影响输出结果
    print(line.strip().replace('Python','C++')) #replace不会改变原字符串内容，因此需要在输出处进行替换