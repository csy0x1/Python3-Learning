class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    
    def describe_restaurant(self):
        print('Restaurant name: '+self.restaurant_name)
        print('Cuisine type: '+self.cuisine_type)
    
    def open_restaurant(self):
        print(self.restaurant_name+' is now in business!')

test=Restaurant('test1','Chinese')
test.describe_restaurant()
test.open_restaurant()

test2=Restaurant('Python','C++')
test2.describe_restaurant()
test2.open_restaurant()

test3=Restaurant('Java','C#')
test3.describe_restaurant()
test3.open_restaurant()