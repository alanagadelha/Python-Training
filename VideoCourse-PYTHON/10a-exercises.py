import random
num = random.randint(0, 5)
user = str(input('Chose a number between 1 and 5: '))

if(num == user):
    print('You have chosen {} and the Computer {}'.format(user, num))
    print('In this case you won the game!!! Congrats')
else:
    print('You have chosen {} and the Computer {}'.format(user, num))
    print('In this case you lose the game!!! Sorry \U0001F923')

