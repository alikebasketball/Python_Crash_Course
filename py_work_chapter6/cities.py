#  Assignment 6-11; Cities
# Create a dictionary called cities, use the name of three cities
# as keys in your dictionary

# Create dictionary
cities = {
    'goldsboro': {
        'country': 'united states of america',
        'population': '32,749',
        'traffic': 'bad',
    },
    'kinston': {
        'country': 'united states of america',
        'population': '19,546',
        'traffic': 'good',
    },
    'raleigh': {
        'country': 'united states of america',
        'population': '469,124',
        'traffic': 'awful',
    }
}

for k, v in cities.items():
    print(f'City: {k.title()}')
    place = f"{v['country']}"
    pop = f"{v['population']}"
    traf = f"{v['traffic']}"
    
    print(f'\tCountry: {place.title()}')
    print(f'\tPopulation: {pop}')
    print(f'\tTraffic Level: {traf.title()}')