import _csv

chs = int(input("Прочитать или записать файл? \n 1.Прочитать \n 2.Записать \n"))
if chs == 1:
    max = int(input("Сколько строк вывести из файла: "))
    k = 0
    with open('test.csv') as f:
        f_csv = _csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            print(row)
            k=k+1
            if k == max:
                break
        input()
elif chs == 2:
    headers = ['Symbol', 'Price', 'Date', 'Time']
    rows = [('AA', 39, '02/02/2020', '00:00'), ('BB', 36, '03/03/2020', '00:12'), ('CC', 23, '04/05/2020', '12:34')]

    with open('test2.csv', 'w') as f:
        f_csv = _csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

    input("Файл создан!")
else:
    print("Ошибка! Введите число 1 или 2!")