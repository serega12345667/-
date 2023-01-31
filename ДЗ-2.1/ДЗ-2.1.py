number = int(input('Введите число в диапазоне от 1 до 100: '))
if number < 0 or number > 100:
    print('Ошибка, введите корректное значение!')
elif number % 3 == 0 and number % 5 == 0:
    print('Fizz Buzz')
elif number % 3 != 0 and number % 5 != 0:
    print(number)
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')


number1 = int(input('Введите число: '))
a = number1 ** 0
b = number1 ** 1
c = number1 ** 2
d = number1 ** 3
e = number1 ** 4
f = number1 ** 5
g = number1 ** 6
h = number1 ** 7
print(a, b, c, d, e, f, g, h, sep="; ")


operator1 = str(input('Введите название Вашего оператора(MTS, TELE2, YOTA): '))
operator2 = str(input('Введите название оператора куда Вы звоните(MTS, TELE2, YOTA): '))
time = int(input('Введите сколько минут Вы будете разговаривать: '))
MTS_MTS = 2
MTS_YOTA = 3
MTS_TELE2 = 6
YOTA_YOTA = 3
YOTA_MTS = 5
YOTA_TELE2 = 7
TELE2_TELE2 = 4
TELE2_MTS = 6
TELE2_YOTA = 8
if operator1 == 'MTS' and operator2 == 'MTS':
    print('Стоимость звонка: ' + str(MTS_MTS * time))
elif operator1 == 'MTS' and operator2 == 'YOTA':
    print('Стоимость звонка: ' + str(MTS_YOTA * time))
elif operator1 == 'MTS' and operator2 == 'TELE2':
    print('Стоимость звонка: ' + str(MTS_TELE2 * time))
elif operator1 == 'YOTA' and operator2 == 'YOTA':
    print('Стоимость звонка: ' + str(YOTA_YOTA * time))
elif operator1 == 'YOTA' and operator2 == 'MTS':
    print('Стоимость звонка: ' + str(YOTA_MTS * time))
elif operator1 == 'YOTA' and operator2 == 'TELE2':
    print('Стоимость звонка: ' + str(YOTA_TELE2 * time))
elif operator1 == 'TELE2' and operator2 == 'TELE2':
    print('Стоимость звонка: ' + str(TELE2_TELE2 * time))
elif operator1 == 'TELE2' and operator2 == 'MTS':
    print('Стоимость звонка: ' + str(TELE2_MTS * time))
elif operator1 == 'TELE2' and operator2 == 'YOTA':
    print('Стоимость звонка: ' + str(TELE2_YOTA * time))
else:
    print('Ошибка, введите корректные данные!')


manager1 = int(input('Введите уровень продаж 1 менеджера: '))
if manager1 < 500:
    print('Зарплата менеджера: ' + str(200 + (manager1 * 3) / 100))
elif 500 <= manager1 <= 1000:
    print('Зарплата менеджера: ' + str(200 + (manager1 * 5) / 100))
elif manager1 > 1000:
    print('Зарплата менеджера: ' + str(200 + (manager1 * 8) / 100))
manager2 = int(input('Введите уровень продаж 2 менеджера: '))
if manager2 < 500:
    print('Зарплата менеджера: ' + str(200 + (manager2 * 3) / 100))
elif 500 <= manager2 <= 1000:
    print('Зарплата менеджера: ' + str(200 + (manager2 * 5) / 100))
elif manager2 > 1000:
    print('Зарплата мменеджера: ' + str(200 + (manager2 * 8) / 100))
manager3 = int(input('Введите уровень продаж 3 менеджера: '))
if manager3 < 500:
    print('Зарплата менеджера: ' + str(200 + (manager3 * 3) / 100))
elif 500 <= manager3 <= 1000:
    print('Зарплата менеджера: ' + str(200 + (manager3 * 5) / 100))
elif manager3 > 1000:
    print('Зарплата менеджера: ' + str(200 + (manager3 * 8) / 100))
if manager1 > manager2 and manager1 > manager3:
    if manager1 < 500:
        print('Лучший менеджер номер 1. Итоговая зарплата: ' + str(400 + (manager1 * 3) / 100))
    elif 500 <= manager1 <= 1000:
        print('Лучший менеджер номер 1. Итоговая зарплата: ' + str(400 + (manager1 * 5) / 100))
    elif manager1 > 1000:
        print('Лучший менеджер номер 1. Итоговая зарплата: ' + str(400 + (manager1 * 8) / 100))
elif manager2 > manager3 and manager2 > manager1:
    if manager2 < 500:
        print('Лучший менеджер номер 2. Итоговая зарплата: ' + str(400 + (manager2 * 3) / 100))
    elif 500 <= manager2 <= 1000:
        print('Лучший менеджер номер 2. Итоговая зарплата: ' + str(400 + (manager2 * 5) / 100))
    elif manager2 > 1000:
        print('Лучший менеджер номер 2. Итоговая зарплата: ' + str(400 + (manager2 * 8) / 100))
elif manager3 > manager1 and manager3 > manager2:
    if manager3 < 500:
        print('Лучший менеджер номер 3. Итоговая зарплата: ' + str(400 + (manager3 * 3) / 100))
    elif 500 <= manager3 <= 1000:
        print('Лучший менеджер номер 3. Итоговая зарплата: ' + str(400 + (manager3 * 5) / 100))
    elif manager3 > 1000:
        print('Лучший менеджер номер 3. Итоговая зарплата: ' + str(400 + (manager3 * 8) / 100))
