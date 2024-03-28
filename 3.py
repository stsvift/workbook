letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for position in range(11):
    print('^' * 27)
    for letter in letters:
        if letters.index(letter) % 11 == position:
            print('| ', letter.upper(), letter, ' |', end='')
    print()
print('^' * 27)