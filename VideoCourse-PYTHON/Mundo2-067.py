

while True:
    print("-"*30)
    num = int(input("Choose the table number: "))
    print("-" * 30)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')
