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
