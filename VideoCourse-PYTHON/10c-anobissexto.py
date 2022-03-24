from datetime import date
year = int(input('What year do you want analyse?'))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('The year {} is leap'.format(year))
else:
    print('The year {} is not leap'.format(year))
print('Done baby!')