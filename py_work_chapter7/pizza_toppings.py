# Assignment 7-4; Pizza Toppings
# Computer crashed not retyping disc. xD

print('Welcome to my pizza shop!')

prompt = '''Enter the toppings here: \n Enter 'quit' when finished'''
msg = ('Please tell me the kind of pizza you would like: ')
typ_of_pizza = input(msg)

if typ_of_pizza.isalpha():
    print('Nice choice today my comrade!\n')

else:
    print('At least put some letter down my man..')
    
# List of toppings
top_lst = ['Pepperoni', 'Extra Cheese', 'Mushrooms', 'Onions', 'Sausage', 'Black Olives', 'Green Peppers', 'Pineapple']

print('what kind of toppings would you like today? \n'
      'We have these to choose from: ')

for x in top_lst:
    print(x)

active = True
while active:
    top = input(prompt)
    
    if top.lower() == 'quit':
        break
    
    if top.title() in top_lst:
        print(f'We will add the topping {top.lower()} to the pizza!')
        
    elif top.title() not in top_lst:
        print(f'We will NOT add the topping {top.lower()} to the pizza..')
        continue