# Assignment 9-12; Multiple Modules
# Store the User class and Privileges and Admin classes in 
# separate modules
import users
import privileges

user_one = privileges.Admin('Eric', 'Holland', 22, 99, 99)
user_one.privileges_xxx.show_admin_privileges()