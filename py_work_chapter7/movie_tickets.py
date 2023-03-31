# Assignment 7-5; Movie Tickets
# Write a loop in which you ask users their age, and tell them the cost of the movie


print('Welcome to the movie theater, all tickets are the same price based on age.')

active = True
while active:
    age = input('Do tell me, what is your age?')
    
    if age.isnumeric():
        
        if int(age) < 3:
            print('Free movie for the young bloods!')
            break
        
        elif int(age) >= 3 and int(age) <12:
            print('That will be ten dollars, U.S. of course.')
            break
        
        elif int(age) >= 12:
            print('Dang, you are pretty old, that will be fifteen..')
            break
    else:
        print('Jeez.. This again?')
        continue