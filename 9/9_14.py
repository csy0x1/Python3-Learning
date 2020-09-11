from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        point=randint(1,self.sides)
        print(point)

temp=Die(20)
for x in range(10):
    temp.roll_die()
