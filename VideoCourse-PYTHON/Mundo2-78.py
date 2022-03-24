value = []
for c in range(0, 4):
    value.append(int(input(f'Type a number for the position {c}: ')))
print(f'You have typed the values: {value}')
for i, v in enumerate(value):
    if v == max(value):
        print(f'The maximum value {max(value)} at the position {i}...')
    if v == min(value):
        print(f'The minimum value {min(value)} at the position {i}...')

