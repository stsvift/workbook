import simplejson

chs = int(input("Прочитать или записать файл? \n 1.Прочитать переменную \n 2.Записать файл \n 3.Прочитать файл \n"))

data = {
    'name': 'Max',
    'shares': 100,
    'count': 542.20
}

if chs == 1:
    json_str = simplejson.dumps(data)
    print(json_str)
    input()
elif chs == 2:
    with open('data.json', 'w') as f:
        simplejson.dump(data, f)
        print("Файл записан!")
elif chs == 3:
    with open('data.json', 'r') as f:
        data = simplejson.load(f)
        print(data)

    input()
else:
    print("Ошибка! Введите числа 1, 2 или 3")
