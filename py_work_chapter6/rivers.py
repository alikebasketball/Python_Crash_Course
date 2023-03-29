# Assignment 6-5; Rivers
# Make a dictionary containing three rivers and the country each river runs through

# Create dictionary
rivers = {'nile river': 'egypt',
          'amazon river': 'south america',
          'yellow river': 'china',
          }

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}!')