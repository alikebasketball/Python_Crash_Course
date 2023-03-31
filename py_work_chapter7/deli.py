# Assignment 7-8; Deli
# Create a list of sandwiches, and an empty list for the sandwiches to go

ordered_sandwiches = ['Pastrami', 'Ham', 'Pastrami', 'turkey', 'chicken', 'ketchup', 'peanut butter', 'Pastrami', 'turkey',]
finished_sandwiches = []

while ordered_sandwiches:
    making_sandwiches = ordered_sandwiches.pop()
    
    print(f'Currently on the {making_sandwiches.lower()} sandwich!')
    finished_sandwiches.append(making_sandwiches.lower())
    
print('\nOrder up! \nFor the party that had the: ')

for sand in finished_sandwiches:
    print(f'\t{sand} sandwich!')