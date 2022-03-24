from random import randint

count = 0
while True:
    computer = randint(0, 11)
    num = int(input('Type a number: '))
    choose = str(input("choose even or odd: [E/O]")).strip().upper()[0]
    soma = computer + num
    if soma % 2 == 0:
        EvenOdd = 'E'
        res = 'EVEN'
    else:
        EvenOdd = 'O'
        res = 'ODD'

    if choose == EvenOdd:
        print('You Win!')
        count = count + 1
    else:
        print('You Loose!')

    print(f'You have choosen {num} and the computer choose {computer}. The sum was {soma}. It is {res}.')

    if choose == EvenOdd:
        print('Lets play again: ')
    else:
        print('Game Over')
        print(f'You won {count} times.')
        break
