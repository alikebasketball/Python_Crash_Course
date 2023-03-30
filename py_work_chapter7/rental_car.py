# Assignment 7-1; Rental Car
# Write a program that ask the user what kind of rental car they would like, and print a message about that car.

message = 'Please enter a car you would like me to search for. '
car = input(message)

if car.isalpha():
    print(f'I will try and locate a {car.title()} for you.'
    '\n...'
    '\n...'
    '\n...')
else:
    print(f'Your input of {car} is not valid here..')