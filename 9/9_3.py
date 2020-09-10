class User():
    def __init__(self,first_name,last_name,age,**more_info):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.info={}
        for key,value in more_info.items():
            self.info[key]=value

    def describe_user(self):
        print('first name: '+self.first_name.title())
        print('last name: '+self.last_name.title())
        print('age: '+self.age)
        for key,value in self.info.items():
            print(key+': '+value)
    
    def greet_user(self):
        print('Hello! '+self.first_name.title()+' '+self.last_name.title())

user1=User('Player','BOT','12',is_a_idiot='yes')
user1.greet_user()
user1.describe_user()

user2=User('taylor','swift','31',album1='folklore',album2='Lover',album3='reputation',album4='1989')
user2.greet_user()
user2.describe_user()