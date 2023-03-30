# Assignment 7-3; Multiples of Ten
# Write a program that determines if a number is a multiple of ten

# Create message for input and input function for the data
request_msg = 'Enter a random number. \nI will tell you if it is divisible by ten!'
number = input(request_msg)

if number.isnumeric():
    
    if int(number) % 10 == 0:
        print(f'The value you entered of {number} is divisible by ten!')
    
    else:
        print(f'The value you entered of {number} is NOT divisible by ten..')
        
elif number.isalpha():
    print('Big brain moment..')
    
else:
    print('Enter something, jeez..\nGot a real bright one here.. '
          'dont we al?')