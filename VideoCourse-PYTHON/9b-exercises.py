num = int(input('Type a number: '))
u = num // 1 % 10
t = num // 10 % 10
h = num // 100 % 10
th = num // 1000 % 10
print('Analysing the number {}'.format(num))
print('The Unit: {}, ten: {}, hundred {}, thousand {}'.format(u, t, h, th))