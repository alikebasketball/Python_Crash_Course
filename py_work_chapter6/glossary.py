# Assignment 6-3; Glossary
# Mimicking a dictionary w/ dictionaries!

definitions = {
    'variable': 'a symbolic name that is a reference or pointer to an object',
    'method': 'a function that “belongs to” an object',
    'object': 'a collection of data (variables) and methods (functions)',
    'function': 'a block of code which only runs when it is called',
    'loop': 'repeating something over and over until a particular condition is satisfied',
}
for keys, value in definitions.items():
    if keys == 'variable':
        print(f'The definition of {keys} is: \n \t{definitions["variable"]} \n')
    elif keys == 'method':
        print(f'The definition of {keys} is: \n \t{definitions["method"]} \n')
    elif keys == 'object':
        print(f'The definition of {keys} is: \n \t{definitions["object"]} \n')
    elif keys == 'function':
        print(f'The definition of {keys} is: \n \t{definitions["function"]} \n')
    elif keys == 'loop':
        print(f'The definition of {keys} is: \n \t{definitions["loop"]} \n')