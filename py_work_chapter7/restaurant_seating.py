# Assignment 7-2; Restaurant Seating
# Write a program that ask the user how many people are in their dinner group

# Create message for input and input function for the data
message_input = 'How many are with you today?'
number_of_ppl = (input(message_input))

if number_of_ppl.isnumeric():
    
    number_of_ppl = int(number_of_ppl)
    
    if number_of_ppl > 8:
        
        print('''Sorry! You'll have to wait in line...''')
        
    else:
        
        print('Right this way!')
        
elif number_of_ppl.isalpha():
    
    print('Only numbers please!!!')

else:
    
    print('Why no input...')