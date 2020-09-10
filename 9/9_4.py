class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    
    def describe_restaurant(self):
        print('Restaurant name: '+self.restaurant_name)
        print('Cuisine type: '+self.cuisine_type)
    
    def open_restaurant(self):
        print(self.restaurant_name+' is now in business!')

    def show_number_served(self):
        print('Restaurant has served '+str(self.number_served)+' people! ')

    def set_number_served(self,number):
        self.number_served=number

    def increment_number_served(self,pplnum):
        self.number_served+=pplnum

test=Restaurant('test1','Chinese')
test.number_served=2563
test.describe_restaurant()
test.open_restaurant()
test.show_number_served()
test.set_number_served(54)
test.show_number_served()
test.increment_number_served(10)
test.show_number_served()