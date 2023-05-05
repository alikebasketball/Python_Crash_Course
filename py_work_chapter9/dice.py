# Assignment 9-13; Dice
# MAKE A DICE!! HAHA AWESOME

# Let us import random..
import random

# Now let us create a dice class
class Dice():
    """This is a simple attempt at making a dice!!
    """
    def __init__(self):
        """This is initializing the dice attributes
        """
        self.sides = 6
        
    def change_side_number(self, NewNumOfSides):
        """Changes the number of sides a dice has

        Args:
            NewNumOfSides (int): Change the dice sides!
        """
        if self.sides < 100:
            self.sides = NewNumOfSides
            
        else:
            print('Never seen more than a 100 sided dice..')
    
    def roll_dice(self):
        return random.randint(1, self.sides)


increment = 1
while increment in range(1, 11):
    
    flag = Dice()
    flag.change_side_number(20)
    print(flag.roll_dice())
    
    increment += 1