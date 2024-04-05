def help_bool(letter=None):
    if letter == 'к':
        return 'A or B = B or A\nA and B = B and A'
    elif letter == 'а':
        return 'A or (B or C) == (A or B) or C == A or B or C\n' \
               'A and (B and C) == (A and B) and C == A and B and C'
    elif letter == 'д':
        return 'A and (B or C) == (A and B) or (A and C) \nA or (B and C) == (A or B) and (A or C)'
    elif letter == 'м':
        return 'not(A or B) == not A and not B \nnot(A and B) == not A or not B\n'\
               'not(A < B) == A >= B\nnot(not(A)) = A'
    else:
        return 'Возможные аргументы: к – Коммутативность, д – Дистрибутивность, а – Ассоциативность, ' \
           'м – Теорема Де Моргана'
print(help_bool())
print(help_bool([2, 6]))
print(help_bool('к'))