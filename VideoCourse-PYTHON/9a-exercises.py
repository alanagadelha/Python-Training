name = str(input('Type your full name: ')).strip()
print('Analysing your name...')
print('Your name in uppercase is {}'.format(name.upper()))
print('Your name in lowercase is {}'.format(name.lower()))
print('Your full name has {} letters'.format(len(name) - name.count(' ')))
print('Your first name has {}'. format(name.find(' ')))
firstname = name.split()
print('Your first name is {} and has {} letters'.format(firstname[0], len(firstname[0])))
print(firstname)
lastname = name.split()
print('Your last name is {} and has {} letters'.format(lastname[4], len(lastname[4])))