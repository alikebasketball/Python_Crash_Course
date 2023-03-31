# Assignment 7-10; Dream Vacation
# Write a program that polls the users

responses_dic = {}

active = True
while active:
    name = input('Hey you! Wanna be apart of something great? Tell me, what is your name..')
    
    if name.isalpha():
        response = input('Good.. Where do you wanna go..')
        
        if response.isalpha():
            
            responses_dic[name] = response
    
            repeat = input('Would you like to let someone else go? (yes / no)')
    
            if repeat.isalpha:
        
                if repeat.lower() == 'yes':
                    continue
                
                elif repeat.lower() == 'no':
                    break
            else:
                print('''It's a yes or no question...''')
        else:
            print('Really bro...')
    else:
        print('Name please...')
    
    
            
    
for name, response in responses_dic.items():
    print(f'So.. {name}.. You wanna go to {response} huh.. ')
    

# I know this isn't exactly what was wanted form the book, but it was fun and was similar!