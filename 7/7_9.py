sandwich_order=['a','b','c','d','e','pastrami','pastrami','pastrami']
finish_sandwich=[]
print('pastrami is sell out')
while sandwich_order:
    #for sandwich in sandwich_order:  不要在for循环内修改列表、字典
    sandwich=sandwich_order.pop()
    if sandwich !='pastrami':
        print('i made you a '+sandwich)
        finish_sandwich.append(sandwich)
print('\nhere is the finished sandwich')
for sandwich in finish_sandwich:
    print(sandwich)