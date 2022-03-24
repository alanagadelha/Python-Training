from random import randint
numbers = (randint(1,10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10) )
print('The numbers chosen were: ', end='')
for n in numbers:
    print(f'{n} ', end='')
print(f'\n 9+The maximum number is {max(numbers)} and the minimum number is {min(numbers)}' )