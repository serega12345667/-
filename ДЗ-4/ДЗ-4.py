x = int(input("Введите диапазон для поиска простых чисел: "))
for num in range(2, x):
    count = 0
    y = 2
    while y < num:
        if num % y == 0:
            count += 1
        y += 1
    if count == 0:
        print(f'{num} простое число')


x = int(input('Введите первое число для таблици умножения: '))
y = int(input('Введите второе число для таблици умножения: '))
z = 0
for i in range(x, y + 1):
    for z in range(1, 11):
        print(f'{i} * {z} = {i * z}', end='\t')
    print()
