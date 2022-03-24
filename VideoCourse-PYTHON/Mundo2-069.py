#This program was created for a valid data!
#How many people has above the 18 years old?
#How many man was validated?
#How many women's has below the 20 years old?
count = countM = countF = 0
while True:
    print('-'*30)
    texto = 'REGISTER A PERSON'
    print(f'{texto: ^30}')
    print('-'*30)

# Treating the age as an integer!
    while True:
        try:
            age = int(input('Type your age: '))
            print('Age {} has being registered successful'.format(age))
            break
        except ValueError:
            print('Invalid data, please type your your age between 1-100 years:')

# Treating the Gender!
    gender = str(input('Type your gender [F/M]: ')).strip().upper()[0]
    while gender not in 'FM':
        gender = str(input('Invalid data, please type your gender [F/M]: ')).strip().upper()[0]
    print('Gender {} register successful'.format(gender))

    if age >= 18:
        count = count + 1
    if gender == 'M':
        countM = countM + 1
    if gender == 'F' and age <= 20:
        countF = countF + 1

    response = str(input('Do you want to continue? [Y/N]')).strip().upper()[0]
    while response not in 'YN':
        response = str(input('Invalid data, do you want to continue? [Y/N]')).strip().upper()[0]
    if response == 'N':
        break

print('Person register above 18s: {}'.format(count))
print('Man register: {}'.format(countM))
print('Womens register below 20s: {}'.format(countF))
