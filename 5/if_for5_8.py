users=['user1','user2','user3','user4','admin']
i=input()
if i=='1':
    users=[]
if users:
    for user in users:
        if user=='admin':
            print('hi admin')
        else:
            print('hi'+user)
else:
    print('we need users')

new_users=['user1','user2','a','c','d']
for user in new_users:
    if user.lower() in users:
        print('need a new username')
    else:
        print('username available')