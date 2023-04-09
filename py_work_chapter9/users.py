# Assignment 9-3; Users
# Make a class called users, with two attributes called
# first_name and last_name and then create several other 
# attributes usually stored in a user profile

# First lets make our class
class User():
    """This is a class that will create a user profile based on
    the inputs for each argument.
    """
    
    def __init__(self, first_name, last_name, age, threat_level, power_level):
        """initializes the attributes

        Args:
            first_name (str): First Name
            last_name (str): Last Name
            age (int): Age
            threat_level (int): Threat Level
            power_level (int): Power Level
        """
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.threat_level = threat_level
        self.power_level = power_level
        
    def describe_user(self):
        print(f'\tFirst Name: {self.first_name.title()}')
        print(f'\tLast Name: {self.last_name.title()}')
        print(f'\tAge: {self.age}')
        print(f'\tThreat Level: {self.threat_level}')
        print(f'\tPower Level: {self.power_level}')
        
    def greet_user(self):
        print(f'Hello, {self.first_name.title()}..')
        print('Your user profile is here: ')
        

# Now lets create instances
U1 = User('eric', 'holland', 22, 99, 99)
U2 = User('jack', 'daniels', 45, 0, 999)
U3 = User('erin', 'zimmerman', 21, 99999, 999)
U4 = User('andrew', 'jackson', 247, 0, 99999999)
U5 = User('george', 'washington', 400, 0, 999999999999999)

U1.greet_user()
U1.describe_user()

U2.greet_user()
U2.describe_user()

U3.greet_user()
U3.describe_user()

U4.greet_user()
U4.describe_user()

U5.greet_user()
U5.describe_user()