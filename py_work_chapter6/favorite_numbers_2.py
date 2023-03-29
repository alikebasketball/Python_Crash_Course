# Assignment 6-10; Favorite Numbers
# Modify program from exercise 6-2

import random as rnd

fav_nums = {
    'john': [1],
    'jack': [2],
    'taylor': [3],
    'sam': [4],
    'jessie': [5],
}
print(fav_nums)

for value in fav_nums.values():
    for v in range(1,5):
        value.append(rnd.randint(1,20))
print(fav_nums)
