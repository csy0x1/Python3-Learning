from user import User

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