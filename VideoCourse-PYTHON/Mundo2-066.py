sum = n = 0
while True:
    num = int(input('Type a number: '))
    if num == 999:
        break
    n = n + 1
    sum = sum + num
print(f'You have typed {n} numbers and the sum is {sum}')
