x = int(input('Введите первое целое число: '))
y = int(input('Введите второе целое число: '))
print(x ** y)


x = 0
i = 0
for i in range(100, 1000):
    a, b, c = str(i)
    if a == b or a == c or b == c:
        x += 1
print(x)


f = 0
y = 0
i = 0
for i in range(100, 1000):
    a, b, c = str(i)
    if a != b and a != c and b != c:
        y += 1
for r in range(1000, 10000):
    a, b, c, d = str(r)
    if a != b and a != c and a != d and b != c and b != d and c != d:
        f += 1
g = y + f
print(g)


x = int(input('Введите число: '))
i = 0
y = 0
while x:
    if not x % 10 in (3, 6):
        y += (x % 10) * 10**i
        i += 1
    x //= 10
print(y)


