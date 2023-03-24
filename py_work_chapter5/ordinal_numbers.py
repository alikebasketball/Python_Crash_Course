# Assignment 5-11; Ordinal Numbers
numbers = list(range(1,10))

if numbers:
    for number in numbers:
        if number == 1:
            print(f'{number}st')
        elif number == 2:
            print(f'{number}nd')
        elif number == 3:
            print(f'{number}rd')
        elif number >3 and number <10:
            print(f'{number}th')
        else:
            print('Not a valid number in given range..')
else:
    print('Please give nums....')