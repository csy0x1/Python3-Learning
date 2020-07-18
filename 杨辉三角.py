def triangles():
    a = [1] #初始行
    while True:
        yield a #输出行
        a = [a[i]+a[i+1] for i in range(len(a)-1)]
        '''
        第二行range为0，得a=[a[0]+a[1]]=[]  因为a[1]超出范围
        第三行range为1，得a=[(a[0]+a[1])+(a[1]+a[2])]=[2]
        '''
        a.insert(0, 1) #在开头插入1
        a.append(1) #在末尾插入1

'''
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
'''