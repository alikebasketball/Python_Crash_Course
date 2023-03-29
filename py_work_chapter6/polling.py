# Assignment 6-6; Polling
# Make a list of people who should take the favorite languages poll

# Create list and dictionary
people_polling = ['jack', 'joe', 'alfred', 'jen', 'sarah', 'edward', 'ezio', 'phil']
favorite_languages_responses = {'jen': 'python',
                                'sarah': 'c',
                                'edward': 'rust',
                                'phil': 'python',
                                }
if people_polling:
    for people in people_polling:
        if people in favorite_languages_responses.keys():
            print(f'Thank you, {people.title()} for taking our poll!')
        elif people not in favorite_languages_responses.keys():
            print(f'Hey {people.title()}, if you have a moment, why not take our poll?')