value = []
answer = 'Y'
while answer in 'Yy':
   n = int(input('Type a number'))
   if n not in value:
       value.append(n)
   else:
       print('Duplicate number, try another')
   answer = str(input('Do you want to continue? [Y/N]')).strip().upper()[0]
print(f'You have typed {value}')
value.sort()

sleep (3)
num[2] = 3

num.sort(reverse=True)
num.insert(2, 0)
if 4 in num:
    num.remove(4)
else:
    print('5 nao esta na lista')
num.pop()
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'At position {c} was found {v}')