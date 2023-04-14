# Assignment 9-6; Ice Cream Stand
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote

from three_restaurants import Restaurant

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initializes the attributes of the parent class
Then attributes related to a specific type of restaurant
        Args:
            restaurant_name (str): Displays a sentence relating to the name 
            cuisine_type (str): Displays a sentence relating to the Cuisine 
        """
        
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint chocolate chip']
        
    def flavor_choices(self):
        for flavor in self.flavors:
            print(flavor.title())
                
ice = IceCreamStand('Happy Place','Chicken Tenders')
print('We have the following flavors: ')
ice.flavor_choices()