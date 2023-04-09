# Assignment 9-1; Restaurant
# Make a class called Restaurant

class Restaurant:
    """This is a class that can create instances of a 
    restaurant and prints the name and cuisine type.
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    
    def describe_restaurant(self):
        """This will hold the restaurants name and the
        cuisine type they have.
        """
        print(self.restaurant_name)
        print(self.cuisine_type)
        
    
    def open_restaurant(self):
        """this method will hold code to print out weather a restaurant
        is open.
        """
        print(f'The restaurant {self.restaurant_name} is open!')
        
    
restaurant = Restaurant('''Holland's World!''', 'Chicken Tenders Only!')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.open_restaurant()