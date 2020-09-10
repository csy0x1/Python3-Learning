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

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=[]

    def show_icecream(self):
        print('we have these flavors of ice cream')
        for flavor in self.flavors:
            print(flavor)

test=IceCreamStand('test ice cream','ice cream')
test.flavors=['a','b','c','d']
test.describe_restaurant()
test.open_restaurant()
test.show_icecream()