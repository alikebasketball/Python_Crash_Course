# Assignment 9-14; Lottery
# Lottery BABYYYY!

# Let us import..
import random

# Lets make some list
lst_one = [*range(1, 70, 1)]
drawing = random.Random().choices(lst_one, k=5)


print(f'If your ticket is equal to {drawing} you win!')


increment = 1
active = True
while active:
    
    my_ticket = random.Random().choices(lst_one, k=5)
    
    if my_ticket == drawing:
        print('''LET'S GOOOOOOOOOOO!''')
        print(f'It took {increment} many tries to win..')
        break
    else:
        print(f'on attempt {increment}')
        increment = increment + 1
        continue