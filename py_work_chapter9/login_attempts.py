# Assignment 9-5; Login Attempts
# Add an attribute to class from assignment 9-3

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
        self.login_attempts = 1
        
    def describe_user(self):
        print(f'\tFirst Name: {self.first_name.title()}')
        print(f'\tLast Name: {self.last_name.title()}')
        print(f'\tAge: {self.age}')
        print(f'\tThreat Level: {self.threat_level}')
        print(f'\tPower Level: {self.power_level}')
        
    def greet_user(self):
        print(f'Hello, {self.first_name.title()}..')
        print('Your user profile is here: ')
    
    def show_login_attempts(self):
        print(f'You are on login attempt {self.login_attempts}..')
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        print('Your Login Attempts Have Been Reset..')
        self.login_attempts = 1


# Now lets create instances
U1 = User('eric', 'holland', 22, 99, 99)

# Show we are on attempt one
U1.show_login_attempts()

# Increase login attempts artificially
while U1.login_attempts in range(1, 10):
    U1.increment_login_attempts()

# Show new login attempt
U1.show_login_attempts()

U1.reset_login_attempts() # Reset attempts
U1.show_login_attempts() # Last showing