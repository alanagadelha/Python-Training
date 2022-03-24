import time

### table ###
num = int(input('Digite um número:'))
for c in range(1,11):
    print('{} X {:2} = {}'.format(num, c, num*c))

import os
os.system("pause")

# Sum of sixth odd numbers#
sum = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um numero:'))
    if num % 2 == 0:
        sum = sum + num
        cont = cont + 1
print('You type {}º odd numbers and the sum is: {}'.format(cont, sum))

import os
os.system('pause')

# Arithmetic Progression
firstAP = int(input('First term: '))
commondifference = int(input('Type a common difference: '))
nthterm = firstAP + (10 - 1) * commondifference
for c in range(firstAP, nthterm, commondifference):
    print('{}'.format(c), end='=> ')
print('End')

import os
os.system('pause')

for c in range(10, 0, -1):
    print(c)
    #time.sleep(1)
print('Feliz ano novo!')

for d in range(0, 51, 1):
    if (d % 2 == 0):
        print(d)


print("-"*30)
lista = []
soma = 0
for e in range(1, 500, 2):
    if (e % 3 == 0):
        soma = soma + e

#        print(e)
#        lista.append(e)
#print(lista)
        print(soma)

#soma2 = 0
#for f in range(0, 7, 1):
    #    m = int(input('Digite um numero: '))
    #if(m % 2 == 0):
#    soma2 = soma2 + m
#print(soma2)

pt = int(input("digite um numero inteiro: "))
ra = int(input("digite a razão (inteiro):"))

for i in range(pt, pt + 10 * ra, ra):
    print(i)
