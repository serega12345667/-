day = int(input('Давайте определим название дня недели. Введите номер дня недели: '))
if day == 1:
    print('Понедельник')
elif day == 2:
    print('Вторник')
elif day == 3:
    print('Среда')
elif day == 4:
    print('Четверг')
elif day == 5:
    print('Пятница')
elif day == 6:
    print('Суббота')
elif day == 7:
    print('Воскресенье')
else:
    print('Введите корректное значение!')


month = int(input('Давайте определим название месяца. Введите номер месяца: '))
if month == 1:
    print('Январь')
elif month == 2:
    print('Февраль')
elif month == 3:
    print('Март')
elif month == 4:
    print('Апрель')
elif month == 5:
    print('Май')
elif month == 6:
    print('Июнь')
elif month == 7:
    print('Июль')
elif month == 8:
    print('Август')
elif month == 9:
    print('Сентябрь')
elif month == 10:
    print('Октябрь')
elif month == 11:
    print('Ноябрь')
elif month == 12:
    print('Декабрь')
else:
    print('Введите корректное значение!')


number = int(input('Введите число: '))
if number > 0:
    print('Number is positive')
elif number < 0:
    print('Number is negative')
else:
    print('Number is equal to zero')


number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
if number1 > number2:
    print(number2, number1, sep="")
elif number1 < number2:
    print(number1, number2, sep="")
else:
    print('Числа являються равными')


