# Assignment 6-4; Glossary 2
# Mimicking a dictionary w/ dictionaries!

definitions = {
    'variable': 'a symbolic name that is a reference or pointer to an object',
    'method': 'a function that “belongs to” an object',
    'object': 'a collection of data (variables) and methods (functions)',
    'function': 'a block of code which only runs when it is called',
    'loop': 'repeating something over and over until a particular condition is satisfied',
    'lambda': 'lambda is a keyword in Python for defining the anonymous function. argument(s) is a placeholder, that is a variable that will be used to hold the value you want to pass into the function expression.',
    'while': 'A while statement in python sets aside a block of code that is to be executed repeatedly until a condition is falsified.',
    'data type': 'Data types are the classification or categorization of knowledge items.',
    'dictionaries': '''Dictionaries are Python's implementation of a data structure that is more generally known as an associative array.''',
    'conditional': 'A conditional statement as the name suggests itself, is used to handle conditions in your program.'}
for keys, value in definitions.items():
    print(f'{keys.title()}: {value}') 