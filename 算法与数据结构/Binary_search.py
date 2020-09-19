#二分查找

def binary_search(list,item):
    low=0 #查找起点
    high=len(list)-1 #查找终点

    while low<=high: #当范围不止一个元素时
        mid=int((low+high)/2) #检查中间元素
        guess=list[mid]
        if guess==item: 
            print(mid)
        if guess>item: 
            high=mid-1 #猜测数字偏大，调整查找终点
        if guess<item:
            low=mid+1 #猜测数字偏小，调整查找起点
        return None

test_list=[1,7,5,8,4]
binary_search(test_list,5) #输出2，即目标为列表第三个元素
binary_search(test_list,3) #无输出，找不到元素
