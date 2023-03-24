# Assignment 5-6; Hello Admin

user_names = ['admin','jacklyn','joe','bob','billy']

if user_names:
    for username in user_names:
        if username.lower() =='admin':
            print(f'Good day {username.title()}, would you like to see the new souls?')
        else:
            print(f'Hello {username.title()}, welcome to hell.')
else:
    print('We need to find some souls!')