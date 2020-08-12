#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

from functools import reduce


def str2float(s):
    i=len(s)-1  #len(s)=7 i=6, i为数字的索引
    while s[i]!=".": #i=3时为'.'，结束循环
        i=i-1
    L1=s[:i] #切片,0~3，不包括3，即不包括'.' 结果为[1,2,3]
    L2=s[i+1:] #切片,结果为[4,5,6]
    DIGITALS={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9} #字典，定义每个字符对应的数字
    def char2num(g):
        return DIGITALS[g]
    def fn(x,y):
        return x*10+y
    r1=reduce(fn, map(char2num, L1))#转换前半部分
    r2=reduce(fn, map(char2num, L2))#转换后半部分
    return r1+r2/10**len(L2) #**代表乘方，即结果为r1+r2/(10^3)=123+456(10^3)=123.456


print('str2float(\'123.456\') =', str2float('123.456'))

if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')