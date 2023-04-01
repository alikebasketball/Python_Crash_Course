# Assignment 8-5; Cities
# Write a function named describe_city() that accepts
# the name of a city and its country

def describe_city(city, country = 'USA'):
    """Function that will return a country and a city

    Args:
        city (string): Any city
        country (str, optional): Any country will do. Defaults to 'USA'.
    """
    print(f'{city.title()} is in the {country.upper()}.')
    
describe_city('detroit')
describe_city('raleigh')
describe_city('moscow', country='russia')