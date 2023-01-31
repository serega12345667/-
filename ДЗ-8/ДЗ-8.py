from itertools import count


def divider(a, b):
    if b == 0:
        return a
    if a > b:
        return divider(b, a % b)
    else:
        return divider(a, b % a)


print(divider(99, 33))

from random import randint

cwe = [randint(1111, 9999) for i in range(1)]
asd = str(cwe)
zz = asd[1:5]
print(zz)


def bull_and_cow(x, count=0):
    count += 1
    bulls = 0
    cows = 0
    for i in range(4):
        if zz[i] == x[i]:
            bulls += 1
        elif x[i] in zz:
            cows += 1
    # print(f' Колличество угаданных цифр: {cows}')
    print(f' Колличество цифр стоящих верно: {bulls}')
    if bulls == 4:
        return f'Ты победил, число {x}  верное! Попыток: {count}'
    return bull_and_cow(str(input('Введите четырёхзначное число: ')), count)



print(bull_and_cow(str(input('Введите четырёхзначное число: '))))
