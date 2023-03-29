# Assignment 6-9; Favorite Places
# Make a dictionary called favorite places, and store one to three
# favorite places for each key

# Create dictionary
favorite_places = {
    'eric': ['united states of america', 'united states of america', 'united states of america'],
    'jacob': ['china', 'wack'],
    'johnathan': ['united states of america']
}

for name, place in favorite_places.items():
    print(f'''\n{name.title()}'s favorite places are:''')
    for location in place:
        print(f'\t{location.title()}')