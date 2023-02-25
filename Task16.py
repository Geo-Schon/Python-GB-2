n = int(input('Введите число: '))
count = 0
for i in range(1, n + 1):
    print(i, end=' ')
    if i == n:
        count += 1
print()
print(count)

# Не до конца понял, что за число X, поэтому сделал так