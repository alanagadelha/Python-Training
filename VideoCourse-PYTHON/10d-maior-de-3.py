a = int(input('First number?: '))
b = int(input('Second number?: '))
c = int(input('Third number?: '))

if a < b and b < c:
    minor = a; print("A is the minor ")
if b < a and b < c:
    minor = b; print('B is the minor')
if c < a and c <b:
    minor = c ; print('C is the minor')
