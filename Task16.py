n = int(input('Введите количество элементов: '))
count = 0
lst = list(map(int, input('Введите элементы списка через пробел: ').split()))

if len (lst) != n:
    print('Условия нарушены! Неправильное количество элементов списка')
else:
    X = int(input('Введите число X: '))
    for i in range(n):
        if lst[i] == X:
            count += 1
    print(f'Число {X} встречается {count} раз')
