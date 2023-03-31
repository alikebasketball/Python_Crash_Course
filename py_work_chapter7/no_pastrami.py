# Assignment 7-9; No Pastrami
# Create a list of sandwiches, and an empty list for the sandwiches to go
# Now remove pastrami


# We are creating our variables here
ordered_sandwiches = ['Pastrami', 'Ham', 'Pastrami', 'turkey', 'chicken', 'ketchup', 'peanut butter', 'Pastrami', 'turkey',]
finished_sandwiches = []

for x in ordered_sandwiches: # We just wanna print out their order first!
    print(f'Your order is {x.lower()}')
    
print('\nSorry! We ran out of pastrami! ... Nerds...\n') # Oops, we ran out..

while 'Pastrami' in ordered_sandwiches: # This is one way to remove an item from a list
    ordered_sandwiches.remove('Pastrami')

if ordered_sandwiches: # Just making sure we still have an order!
    while ordered_sandwiches: # Well, since we do.. lets make them!
        making_sandwiches = ordered_sandwiches.pop()
    
        print(f'Currently on the {making_sandwiches.lower()} sandwich!')
        finished_sandwiches.append(making_sandwiches.lower())
    
print('\nOrder up! \nFor the party that had the: ')

for sand in finished_sandwiches:
    print(f'\t{sand} sandwich!')
    