# Assignment 9-4; Number Served
# Start with program from assignment 9-1

class Restaurant:
    """This is a class that can create instances of a 
    restaurant and prints the name and cuisine type.
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
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
        
    def reading_number_served(self):
        """Number of people served
        """
        print(f'The number of people served today is: {self.number_served}')
    
    def set_number_served(self, set_number_served):
        """Allows us to set the number of people served

        Args:
            number_served (int): Setting the number of ppl served
        """
        if set_number_served >= self.number_served:
            self.number_served = set_number_served
            
        else:
            print('Why you messing with this and it is not increasing..')
        
    def increment_number_served(self, total_inc):
        """allows us to increment the number of people served
            by an increment amount
        Args:
            total_inc (int): number that increases ppl served
        """
        
        if total_inc >= self.number_served:
            self.number_served += total_inc
        
        else:
            print('You can not un-serve people..')

restaurant = Restaurant('Hey', 'Chicken')
restaurant.set_number_served(1)
restaurant.increment_number_served(20)
restaurant.reading_number_served()