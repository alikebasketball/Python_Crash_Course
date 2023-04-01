# Assignment 8-2; Favorite Book
# Write a function called 'favorite_book()' as pass it one argument

def favorite_book(title):
    """ Here we are going to make a function to print out a sentence
    concerning my favorite book!
    """
    message = '''One of my favorite books of all time, is'''
    
    print(f'{message} {title.title()}!')
    
favorite_book('pegasus')