from datetime import date
actualyear = date.today().year
birthdayyear = int(input('Type the year of your birthday: '))
classification = (actualyear - birthdayyear)

if classification < 9:
    print('You have {} years old, therefore you are MIRIM'.format(classification))
elif 10 < classification <= 14:
    print('You have {} years old, therefore you are INFANTIL'.format(classification))
elif 15 < classification <= 19:
    print('You have {} years old, therefore you are JUNIOR'.format(classification))
elif 19 < classification <= 25:
    print('You have {} years old, therefore you are SENIOR'.format(classification))
else:
    print('You have {} years old, therefore you are MASTER'.format(classification))
