# Assignment 8-3; T-Shirt
# Write a function called make_shirt() that accepts size and 
# test that should be printed on the shirt

def make_shirt(size, text):
    """To make a function that will print the size of a shirt,
    and the text on the shirt

    Args:
        size (string): XL, L, M, S, XS
        text (string): Something patriotic
    """
    print(f'I wear a {size} t-shirt.')
    print(f'The shirt should have the text, {text} written on it.')
    
make_shirt('M', "'Make America Great Again!'")
make_shirt(size='M', text="'FJB, Worst Former VP Ever!'")