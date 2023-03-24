# Assignment 5-10; Checking Usernames
current_users = ['Daniels','Jack','bob','billy','joe']
new_users = ['Daniels','Jack','beth','sam','sally']
new_list = [current_user.lower() for current_user in current_users]



if new_users:
    for new_user in new_users:
        if new_user.lower() in new_list:
            print('Sorry, that username is already taken.. -10 to intelligence')
        else:
            print('That username is available!')
else:
    print('No new users today..')