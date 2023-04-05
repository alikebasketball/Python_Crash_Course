# Assignment 8-13; User Profile
# Start with a copy of the user_profile.py from page 148

def build_profile(first, last, **user_info):
    """A function that will build a user profile in a dictionary

    Args:
        first (str): first name
        last (str): last name
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('eric', 'holland',
                             height =  'short',
                             muscles = 'big',
                             strength = 'strong')

print(user_profile)