def divider(a, b):
    return b and (a / b) ** 3 or 'Нули в знаменателе не приветствуются'
print(divider(10, 4))
print(divider(10, 0))
print(divider(-12.2, 2))
print(divider(-6.4, 0))