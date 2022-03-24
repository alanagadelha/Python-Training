from num2words import num2words
#extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco')
num = int(input('Type a value between 0 and 5: '))
while num not in range(0, 6):
    num = int(input('Invalid value. Try again: '))

print(num2words(num, lang='en'))
