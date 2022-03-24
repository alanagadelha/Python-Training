num1 = int(input('Type the first number: '))
num2 = int(input('Type the second number: '))
options = 0
while options != 5:
    print('you have typed the number {} and {}'.format(num1, num2))
    print('''your options:
    [ 1 ] = sum
    [ 2 ] = multiple
    [ 3 ] = greater 
    [ 4 ] = new numbers 
    [ 5 ] = exit
    ''')
    options = int(input('Type your option: '))

    if options == 1:
        sum = num1 + num2
        print('The sum is {}'.format(sum))
    if options == 2:
        x = num1 * num2
        print('The multiplication is {}'.format(x))
    if options == 3:
        if num1 > num2:
            print('The first number is greater than second number')
        else:
            print('The second number is greater than first one')
    if options == 4:
        num1 = int(input('Type the first number: '))
        num2 = int(input('Type the second number: '))
    if options == 5:
        print('exit')
