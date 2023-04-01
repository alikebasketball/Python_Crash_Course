# Assignment 8-4; Large Shirts
# Edit the previous function

def make_shirt(size='L', text='I Love Python!'):
    """To make a function that will print the size of a shirt,
    and the text on the shirt

    Args:
        size (string): XL, L, M, S, XS
        text (string): Something patriotic
    """
    print(f'I wear a {size} t-shirt.')
    print(f'''The shirt should have the text, '{text}' written on it.''')
    
make_shirt()
make_shirt(size='M')
make_shirt(size='XL',text='Fight For Your Freedoms!')