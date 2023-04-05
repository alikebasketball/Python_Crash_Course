# Assignment 8-10; Sending Messages
# Start with code from the previous example, 
# Add some flair, move the message as its passed

# Create list
lst_of_messages = ['Hello, World!', 'welcome to my murder party!', 'knowledge is power', 'welcome to the matrix..']
lst_of_sent_msgs = []

def transfer_of_msgs(lst_one, lst_two):
    
    """This is a function designed to move one element in a list of strings
    to another.
    """
    
    while lst_one:
        msg = lst_one.pop()
        lst_two.append(msg)
        
        
def callouts(lst_of_sent):
    """This functioned is designed to print out the list now containing
    the contents of the previous one.

    Args:
        lst_of_sent (str): new list with the old data
    """
    for msg in lst_of_sent:
        print(f'''The message '{msg.title()}' has been sent.''')
        
        
        
transfer_of_msgs(lst_of_messages, lst_of_sent_msgs)

callouts(lst_of_sent_msgs)