points_en = {1: 'AEIOULNSTR',
             2: 'DG',
             3: 'BCMP',
             4: 'FHVWY',
             5: 'K',
             8: 'JZ',
             10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ',
             2: 'ДКЛМПУ',
             3: 'БГЁЬЯ',
             4: 'ЙЫ',
             5: 'ЖЗХЦЧ',
             8: 'ШЭЮ',
             10: 'ФЩЪ'}

n = int(input('Если хотите играть на английском введите - 1, если на русском - 0: '))
word = input('Введите слово: ').upper()
if n == 1:
    print('Вы получаете', sum([j for i in word for j, k in points_en.items() if i in k]), 'очков')
elif n == 0:
    print('Вы получаете', sum([j for i in word for j, k in points_ru.items() if i in k]), 'очков')
else:
    print('Это что-то новенькое')
