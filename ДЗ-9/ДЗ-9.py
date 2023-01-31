from random import randint
spisok = [randint(-10, 10) for i in range(9)]
print(spisok)
spisok_1 = spisok[0:6]
spisok_3 = spisok[0:3]
spisok_4 = spisok[3:]
spisok_2 = spisok[6:]
a = sum(spisok[0:6])//6
if a > 0:
    spisok_1.sort()
    print(spisok_1 + spisok_2[::-1])
else:
    spisok_3.sort()
    print(spisok_3 + spisok_4[::-1])


a = int(input('Введите оценку по математике(от 1 до 12): '))
b = int(input('Введите оценку по русскому языку(от 1 до 12): '))
c = int(input('Введите оценку по литературе(от 1 до 12): '))
d = int(input('Введите оценку по географии(от 1 до 12): '))
e = int(input('Введите оценку по физике(от 1 до 12): '))
f = int(input('Введите оценку по физ-ре(от 1 до 12): '))
g = int(input('Введите оценку по ОБЖ(от 1 до 12): '))
h = int(input('Введите оценку по ИЗО(от 1 до 12): '))
team = 1
evaluations = []
evaluations.extend((a, b, c, d, e, f, g, h))
while team > 0:
    team = int(input('Если Вы хотите вывести оценки, введите 1; '
                     'Если Вы хотите пересдать экзамен, введите 2; '
                     'Если Вы хотите узнать будет ли степендия, введите 3; '
                     'Если Вы хотите увидеть отсортиорванный список по возростанию, введите 4; '
                     'Если Вы хотите увидеть отсортиорванный список по убыванию, введите 5; '
                     'Для завершения программы введите 0: '))
    if team == 1:
        print(f' Математика: {a} \n Русский язык оценка:  {b} \n Литература оценка: {c} '
              f'\n География оценка: {d} \n Физика оценка: {e} \n Физ-ра оценка: {f} \n ОБЖ оценка: {g}'
              f' \n ИЗО оценка: {h}')
        print(f'Список оценок: {evaluations}')
    elif team == 2:

        q = int(input('Введите номер элемента списка: '))
        m = int(input('Введите новую отметку: '))
        evaluations[q] = m
        print(evaluations)
    elif team == 3:
        j = sum(evaluations)/8
        if j >= 10.7:
            print(f'Ваш балл: {j}, поздравляем Вам назначена степендия!')
        else:
            print('Степендии не будет!')
    elif team == 4:
        evaluations.sort()
        print(evaluations)
    elif team == 5:
        evaluations.sort()
        print(evaluations[::-1])
print('Благодарим за использование программы, всего доброго!')


from random import randint
spisok = [randint(1, 20) for i in range(10)]
print(spisok)

def sort_1(spisok):
    has_swapped = True
    while (has_swapped):
        has_swapped = False
        for i in range(len(spisok) - 1):
            if spisok[i] > spisok[i + 1]:
                spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
                has_swapped = True
    return spisok


print(sort_1(spisok))
