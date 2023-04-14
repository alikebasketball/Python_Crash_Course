# Assignment 9-9; Battery Upgrade
# Use the final version on electric_car.py from this section

class Car():
    """A simple attempt to represent a car.
    """
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car.

        Args:
            make (str): Make of a car
            model (str): Car model
            year (str): year, using str here as no computations to be made
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name
        """
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name
    
    def read_odometer(self):
        """Print statement showing cars mileage
        """
        print(f'This car has {self.odometer_reading} miles on it.')
        
    def update_odometer(self, mileage):
        """set odometer to a value

        Args:
            mileage (int): mileage value
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        
        else:
            print('''You can't roll back an odometer bro...''')
    
    def increment_odometer(self, miles):
        """Add a given amount to odometer
        """
        self.odometer_reading += miles
        

# Child Class One
class ElectricCar(Car):
    """Represents aspects of an electric car"""
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        
        self.battery = Battery()
        

# Child Class Two
class Battery():
    """A simple attempt to model a battery for an electric car
    """
    
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')
    
    def get_range(self):
        if self.battery_size == 40:
            rng = 150
        
        elif self.battery_size == 65:
            rng = 225
        
        print(f'This car gets about {rng} miles on a full charge..(Weak..)')
        
    def upgrade_battery(self):
        self.battery_size = 65

test_one = ElectricCar('GG', 'RIPZ', 'GZZZ')
test_one.battery.get_range()
test_one.battery.upgrade_battery()
test_one.battery.get_range()