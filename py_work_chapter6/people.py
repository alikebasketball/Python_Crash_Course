# Assignment 6-7; People
# Store three dictionaries in a list called people, loop through the list of people
person_one = {
    'first_name': 'johnathan',
    'last_name': 'castor-pieneda',
    'age': 22,
    'city_lived': 'seven springs',
    }
person_two = {
    'first_name': 'jacob',
    'last_name': 'boomhower',
    'age': 22,
    'city_lived': 'dudley',
    }
person_three = {
    'first_name': 'taylor',
    'last_name': 'jarman',
    'age': 30,
    'city_lived': 'mount olive',
    }

people = [person_one, person_two, person_three]

for person in people:
    for k, v in person.items():
        v = str(v)
        print(f'{k.title()}: {v.title()} \n')