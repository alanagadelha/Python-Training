
# Fibonacci Sequence
# 0 - 1 - 1 - 2 - 3
# t1  t2  t3
#     t1  t2  t3
#         t1  t2 = t1 passa a ser t2 e t2 passa a ser o t3
print('-'*30)
print('Fibonacci sequence!!!')
print('-'*30)
nterms = int(input('How many terms do want to see?: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 0
while cont <= nterms:
 #   t3 = t1 + t2
 #   t1 = t2   print(' -> {}'.format(t3), end='')
 #
 #   t2 = t3
    t3 = (nterms -1) + (nterms -2)
    print(' -> {}'.format(t3), end='')
    cont = cont + 1
