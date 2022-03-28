words = ('coisa', 'alana', 'lilo', 'iva')
for w in words:
    print(f'\nIn the word {w.upper()} we have: ', end='')
    for letters in w:
        if letters.lower() in 'aeiou':
            print(f'{letters}', end='')