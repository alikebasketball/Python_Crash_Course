# Assignment 9-8; Privileges
# Create a separate class called Privileges
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

class Privileges():
    def __init__(self, first_name):
        self.privileges = ['can create post', 'can delete post', 'can ban users', 'can un-ban users']
        self.first_name = first_name
        
    def show_admin_privileges(self):
        with open('admin_users.txt', 'r') as fileObject:
            admin_users = []
            for item in fileObject:
                x = item.strip('\n')
                admin_users.append(x)
             
             
        if self.first_name in admin_users:
            print('Hello, Admin.')
            print('You stand above all others..')
            print('You have special privileges..\nThese are:')
            
            for privilege in self.privileges:
                print(privilege.title())
        else:
            print('Admin names are case sensitive..')

class Admin(User):
    
    def __init__(self, first_name, last_name, age, threat_level, power_level):
        """initializes the attributes of parent class and child class"""
        
        super().__init__(first_name, last_name, age, threat_level, power_level)
        
        self.privileges_xxx = Privileges(first_name)

test_one = Admin('Eric', 'Holland', 22, 99, 99)
test_one.greet_user()
test_one.describe_user()
test_one.privileges_xxx.show_admin_privileges()
