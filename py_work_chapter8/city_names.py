# Assignment 8-6; City Names
# Write a function called city_names() that takes in the name 
# of a city and its country. CAll your function with at least three
# city-country pairs and print the values returned

def city_country(city, country):
    """Returns city and country pairs neatly, and is printed

    Args:
        city (string): Any city
        country (string): Any country (city has to be in this country)
    """
    neat_cityPair = f'{city}, {country}'
    return neat_cityPair.title()

pair_one = city_country('goldsboro', 'united states of america')
pair_two = city_country('kinston', 'united states of america')
pair_three = city_country('smith field', 'united states of america')
print(f'{pair_one}\n{pair_two}\n{pair_three}')