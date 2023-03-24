age = input('Please enter your age, I will tell you what you are: ')
age = int(age)

if age < 2 and age > 0:
    print('You are a baby! HAHA!')
    
elif age >=2 and age <4:
    print('You are a toddler! HAHA!')
        
elif age >= 4 and age <13:
    print('Your just a kid! - Katara TLAB')
    
elif age >= 13 and age <20:
    print('''Well, you're just a teenager.. -Ang TLAB''')
    
elif age >= 20 and age < 65:
    print('Wow, congrats! You made it this far without smoking yourself.')
    
elif age >= 65 and age < 99:
    print('Get of the road..., in fact, how did you get here?')

else:
    print('Not valid Inputs!')