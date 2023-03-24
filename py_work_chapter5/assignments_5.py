# # Assignment 5-1; Conditional Tests
# pizza = 'cheese'
# print(f'If pizza is == cheese I predict True')
# print(pizza == 'cheese')

# print(f'If pizza is != cheese I predict False')
# print(pizza != 'cheese')

# car = 'fast'
# print(f'If car is == fast or cool I predict True')
# print(car == 'fast' or car =='cool')

# print(f'If car is == slow or cool I predict False')
# print(car == 'slow' or car == 'cool')

# my_age = 22
# me = 'cool'
# print('If my age is >= 21 and me is cool, I predict True')
# print(my_age >= 21 and me == 'cool')

# print('If my age is < 21 and me is cool, I predict False')
# print(my_age < 21 and me == 'cool')

# my_traits = ['short','strong','powerful','cool']
# print('If short is in my_traits, I predict True')
# print('short' in my_traits)

# print('If tall is in my_traits, I predict False')
# print('tall' in my_traits)

# awesome_people = ['Eric','taylor','jacob']
# person = 'rando'
# print('If someone other than my friends not in awesome people, I predict True')
# if 'rando' not in awesome_people:
#     print(f'Hey {person.title()}, you suck!')
    
# print('If Eric not in awesome people, I predict False')
# if 'Eric' not in awesome_people:
#     print('This is wrong.. so wrong.')
# else:
#     print('DING DING DING! WE HAVE A WINNER!')

# Assignment 5-3; Alien Colors #1
alien_color = 'green'
if alien_color.lower() == 'green':
    print('Your score was increased by 5!')

alien_color = 'green'
if alien_color.lower() == 'green':
    print('Your score was increased by 5!')
else:
    print('Wow, you just had your score raised by 10!')
    
alien_color = 'red'
if alien_color.lower() == 'green':
    print('Your score was increased by 5!')
else:
    print('Wow, you just had your score raised by 10!')