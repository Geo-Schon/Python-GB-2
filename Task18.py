n = int(input('Введите колиличество элементов: '))
count = 0
lst = []
lst.append(list(map(int, input().split())))

if len (lst) != n or n == 0:
    print('Условия нарушены! Элементы не соотвествуют количеству')
else:
    X = int(input('Введите число X: '))
    for i in range(1, n + 1):
        if lst[i] == X:
            count += 1
    print(f'Число {X} встречается {count} раз')

if len(A_num) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A_num[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A_num[index])}')