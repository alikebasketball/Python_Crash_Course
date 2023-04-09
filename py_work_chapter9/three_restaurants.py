# Assignment 9-2; Three Restaurants
# Start with you class from the previous assignment


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
        print(f'Our restaurants name is {self.restaurant_name}!')
        print(f'We serve {self.cuisine_type} only!')
        
    
    def open_restaurant(self):
        """this method will hold code to print out weather a restaurant
        is open.
        """
        print(f'The restaurant {self.restaurant_name} is open!')
        
first_instance = Restaurant('Hello Place', 'Chicken Tenders')
second_instance = Restaurant('The Good Place', 'Chicken Tenders')
third_instance = Restaurant('The Happy Place', 'Chicken Tenders')

first_instance.describe_restaurant()
second_instance.describe_restaurant()
third_instance.describe_restaurant()