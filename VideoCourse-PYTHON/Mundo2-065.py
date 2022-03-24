sum = 0
answer = 'Y'
while answer in 'Yy':
    num = int(input('Type a number: '))
    answer = str(input('Do you want to continue? [Y/N]')).strip().upper()[0]
    sum = sum + num
    mean = sum/2
    print('The mean of all the numbers is {}'.format(mean))
print('End')
