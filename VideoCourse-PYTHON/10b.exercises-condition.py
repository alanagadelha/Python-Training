print('Firts exercise')
veloc = int(input('Whats your real velocity: '))

if (veloc > 80):
    fine = (veloc - 80) * 7
    print('\033[31m You have exceeded the maximum permitted of velocity \033[m')
    print('\033[33m You will be fined! and you will have to pay R${} reais'.format(fine))
else:
    print('\033[32m Congrats, Drive safely')
print('*='*20)
print('End of the First exercise')
print('*='*20)
print('')
print('Now lets find out if this velocity is even or odd')
print('=>'*30)

num = veloc % 2
print(num)

if num == 0:
    print('The veloc is even')
else:
    num == 1
    print('The veloc is odd')

