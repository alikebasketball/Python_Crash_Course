# Assignment 8-14; Cars
# Write a function that stores information about a car
# into a dictionary, that has 2 required values
# And has an arbitrary amount of arguments

def make_car(manufacturer, model, **kwargs):
    """This function is designed to store information on a car
    into a dictionary that will require two values, and have an
    arbitrary amount of arguments

    Args:
        manufacturer (str): manufacturer of a car
        model (str): model of a car
    """
    
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car = make_car('ford', 'mustang',
              color = 'Neon Orange',
              pack = 'GT')

print(car)