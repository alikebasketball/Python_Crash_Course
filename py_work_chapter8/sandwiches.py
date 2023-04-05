# Assignment 8-12; Sandwiches
# Write a function that accepts a list of items a person wants
# On a sandwich


        
def sandwich(*item):
    print('Your sandwich has the following items on it: ')
    
    for x in item:
        print(f'{x.title()}')
    
sandwich('Jack', 'Daniels')
sandwich('apples', 'oranges', 'tea')
sandwich('apples', 'oranges', 'tea', 'snacks')