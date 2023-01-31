a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a % 2 == 0 and b % 2 == 0:
    print('Сумма четных чисел равна: ' + str(a + b) + ' \nСредне арифимитческое заданных чисел: ' + str((a + b)/2))
elif a % 2 != 0 and b % 2 != 0:
    print('Сумма нечетных чисел равна: ' + str(a + b) + ' \nСредне арифимитческое заданных чисел: ' + str((a + b)/2))
elif a % 2 == 0 and b % 2 != 0:
    print('Нечетное число: ' + str(b) + ' \nЧетное число : ' + str(a) + '. \nСредне арифимитческое заданных чисел: ' + str((a + b) / 2))
elif a % 2 != 0 and b % 2 == 0:
    print('Нечетное число: ' + str(a) + ' \nЧетное число : ' + str(b) + ' \nСредне арифимитческое заданных чисел: ' + str((a + b) / 2))
elif a % 9 == 0 and b % 9 == 0:
    print('Сумма чисел кратных 9 равна: ' + str(a + b) + ' \nСредне арифимитческое заданных чисел: ' + str((a + b) / 2))


c = int(input('Введите длинну линии: '))
d = str(input('Введите символ для заполнения: '))
i = 0
while i < c:
    i += 1
    print(d)


number = 0
while number != 7:
    number = int(input('Введите число: '))
    if number == 7:
        print('Good bye!')
        break
    elif number > 0:
        print('Number is positive')
    elif number < 0:
        print('Number is negative')
    elif number == 0:
        print('Number is equal to zero')
    else:
        print('Good bye!')
        break


while True:
    e = int(input('Введите первое число: '))
    f = int(input('Введите второе число: '))
    if e != 7 and f != 7:
        a = e + f
        print('Сумма чисел: ' + str(a))
        if e > f:
            print('Максимальное число: ' + str(e) + ' Минимальное число: ' + str(f))
        elif e < f:
            print('Максимальное число: ' + str(f) + ' Минимальное число: ' + str(e))
    else:
        print('Good bye!')
        break









