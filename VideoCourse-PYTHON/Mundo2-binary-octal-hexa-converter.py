from typing import Any

number = int(input('Type a integer number: '))
i = number
list = []

while i != 0:
    r = i % 2
    i = i // 2
    list.append(r)
    print('number is', i)
    print('resto', r)
    print(list)
    binary = list[::-1]
    print(binary)

i = number
list = []
while i > 7:
    remainder = i % 8
    i = i // 8
    list.append(remainder)
    print(list)
    octal = list[::-1]
    print(octal)
if i < 8:
    list.append(i)
print(list)

# Conversion table of remainders to
# hexadecimal equivalent
print('=>' * 30)
i = number
list1 = []
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
while i > 0:
    remainder = i % 16
    i = i // 16
    print('i= ', i)
    print('remainder: ', remainder)
    hexadecimal = conversion_table[remainder]
    list1.append(hexadecimal)
    hex = list1[::-1]
print(hex)

print('The binary number is', binary)
print('The octal number is', list)
print('The Hexadecimal number is', hex)

