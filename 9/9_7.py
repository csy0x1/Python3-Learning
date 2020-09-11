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

class Privileges():
    def __init__(self,privileges=[]):
        self.privileges=['can add post','can delete post','can ban user',]

    def show_privileges(self):
        print("Admin's privileges: ")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self,first_name,last_name,age,**more_info):
        super().__init__(first_name,last_name,age,**more_info)
        self.privil=Privileges()#需要前面Privileges类 __init__处设定形参privileges默认值或这里给出实参privileges的值，否则报错

admin=Admin('admin','test','21')
admin.privil.show_privileges()
