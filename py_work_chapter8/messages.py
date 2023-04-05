# Assignment 8-9; Messages
# Create a list of short messages, pass the list to a function to print each message

# Create list
lst_of_messages = ['Hello, World!', 'welcome to my murder party!', 'knowledge is power', 'welcome to the matrix..']

def prt_of_lst(lst_one):
    """Print out content in a list, in this case messages.

    Args:
        lst_one (str): list of strings
    """
    
    for message in lst_one:
        print(message.title())
    
prt_of_lst(lst_of_messages)