gender = str(input('Type your gender [F/M]: ')).strip().upper()[0]
while gender not in 'FfMm':
    gender = str(input('Invalid data, please type your gender [F/M]: ')).strip().upper()[0]
print('Gender {} register successful'.format(gender))




