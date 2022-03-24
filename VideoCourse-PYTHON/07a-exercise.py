n = int(input('Type one number: '))
a = n - 1
s = n+1
#print('Analyzing the number {}, this ancestor is {} and this sucessor is {}'.format(n, a, s))
print('Analysing the number {}, this ancestor is {} and this sucessor is {}'.format(n, n-1, n+1))
print('Analysing the number {}, the double is {} and the triple is {}'.format(n, n*n, n*n*n))
print('Analysing the number {}, the square is {:.4f}'.format(n, n**(1/2)))
print('Analysing the number {}, the square is {:.4f}'.format(n, pow(n,(1/2))))