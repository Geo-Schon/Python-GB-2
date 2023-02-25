n = int(input('Введите колиличество элементов: '))
count = 0
lst = []
lst.append(list(map(int, input().split())))

X = int(input('Введите число X: '))
if len (lst) != n:
    print('Элемент не найден')
else:
    for i in range(1, n + 1):
        if lst[i] == X:
            count += 1
    print(f'Число {X} встречается {count} раз')
