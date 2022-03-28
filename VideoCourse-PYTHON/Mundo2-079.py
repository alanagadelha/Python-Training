numbers = []
response = 'Y'
while response in 'Y':
    numbers = str(input(' Do you want to add new numbers [Y/N]: ')).strip().upper()[0]
print(f'Your new numbers {numbers} was register successful')