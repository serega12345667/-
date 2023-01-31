def text(x):
    return x


print(text('\"Don\'t compare yourself with anyone in this world... '
           '\n if you do so, you are insulting yourself.\" '
           '\n''                                          Bill Gates'))


def even_numbers(x, y):
    for i in range(x, y + 1):
        res = 0
        if i % 2 == 0:
            res += i
            print(res, end=' ')
    print()


even_numbers(7, 28)


def square(x, y, z):
    if z:
        for i in range(x):
            print(y * x)
            i -= 1
    else:
        print(y * x)
        for i in range(x):
            print((y * 1) + (' ' * (x - 2) + y))
            i -= 1
        print(y * x)


square(9, '*', 0)


def number(x, q, w, e, r):
    res = min(x, q, w, e, r)
    return res


print(number(11, 3728, 21, 6542, 77780))


def composition(x, y):
    res = 1
    if x < y:
        for i in range(x, y + 1):
            res *= i
        return res

    else:
        for i in range(y, x + 1):
            res *= i
        return res


print(composition(8, 2))


def count(x):
    res = 0
    while x > 0:
        res += 1
        x //= 10
    return res


print(count(257895549156151623654))


def palindrome(x):
    if str(x) == str(x)[::-1]:
        print('Палиндром')
    else:
        print('Не палиндром')


palindrome(20040004002)
