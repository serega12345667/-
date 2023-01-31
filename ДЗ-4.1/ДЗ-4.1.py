while True:
    a = int(input('Введите цифру от 1 до 10: '))
    if a == 1:
        for i in range(10):
            print(' ' * i + '*' * (9 - i) + '*')
            i -= 1
    elif a == 2:
        for i in range(10):
            print('*' * i + '*')
            i += 1
    elif a == 3:
        for i in range(6):
            print(' ' * i + '*' * (10 - i * 2) + '*' + ' ' * i)
            i -= 1
    elif a == 4:
        for i in range(6):
            print(' ' * (5 - i) + '*' * (i * 2) + '*')
            i -= 1
    elif a == 5:
        for i in range(6):
            print(' ' * i + '*' * (10 - i * 2) + '*' + ' ' * i)
            i -= 1
        for i in range(6):
            print(' ' * (5 - i) + '*' * (i * 2) + '*')
            i -= 1
    elif a == 6:
        for i in range(6):
            print('*' * (1 + i) + ' ' * (5 - i) + ' ' * (5 - i) + '*' * (1 + i))
            i -= 1
        for i in range(6):
            print('*' * (5 - i) + ' ' * (i + 1) + ' ' * (i + 1) + '*' * (5 - i))
            i -= 1
    elif a == 7:
        for i in range(6):
            print('*' * i + '*' + ' ' * i)
            i -= 1
        for i in range(6):
            print('*' * (5 - i) + '*' + ' ' * i)
            i -= 1
    elif a == 8:
        for i in range(6):
            print(' ' * (5 - i) + '*' * i + '*')
            i -= 1
        for i in range(6):
            print(' ' * i + '*' * (5 - i) + '*')
            i -= 1
    elif a == 9:
        for i in range(10):
            print('*' * (9 - i) + '*' + ' ' * i)
            i -= 1
    elif a == 10:
        for i in range(10):
            print(' ' * (10 - i) + '*' * i + '*')
            i += 1
    else:
        print('Введите корректные данные!')












