# Assignment 6-8; Pets
# Make several dictionaries, where each dictionary represents a different pet


# make dictionaries
pet_one = {
    'type': 'dog',
    'owner': 'jack daniels',
    'color': 'red'
}
pet_two = {
    'type': 'cat',
    'owner': 'blue moon',
    'color': 'blue'
}
pet_three = {
    'type': 'bear',
    'owner': 'eric holland',
    'color': 'brown'
}


pets = [pet_one, pet_two, pet_three] # Store in list

for pet in pets:
    for k, v in pet.items():
        if k == 'type':
            print(f'The type of animal I have is a {v}!')
        elif k == 'owner':
            print(f'Oh! My name is {v.title()} by the way!')
        elif k == 'color':
            print(f'The color of my pet is {v}..\n')