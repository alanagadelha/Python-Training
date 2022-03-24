from random import randint
computer = randint(1, 11)
acertou = False
cont = 1
while not acertou:
    player = int(input('Type a number: '))
    cont = cont + 1
    if computer == player:
        acertou = True
        cont = cont + 1
    else:
        if player < computer:
            print('More....')
        elif player > computer:
            print(Less...)
print('The computer had chosen {} and you used {} guess'.format(computer, cont))
