# Assignment 9-14; Lottery
# Lottery BABYYYY!

# Let us import..
import random

# Lets make some list
lst_one = [1,345,457,234,22,55,546,2,45, 'a', 'b', 'c', 'd', 'e']
drawing = random.choices(lst_one, k=4)

print(f'If your ticket is equal to {drawing} you win!')