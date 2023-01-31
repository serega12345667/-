nam = input('Ввидите арифметическое выражение: ').split(' ')
if (nam[1]) == '+':
    a = int(nam[0]) + int(nam[2])
    print(a)
elif (nam[1]) == '-':
    a = int(nam[0]) - int(nam[2])
    print(a)
elif (nam[1]) == '*':
    a = int(nam[0]) * int(nam[2])
    print(a)
elif (nam[1]) == '/':
    a = int(nam[0]) / int(nam[2])
    print(a)


from random import randint
spisok = [randint(-50, 50)
          for i in range(10)]
print(spisok)
sorted_list = sorted(spisok)
result = sorted_list[-1]
print(f'Максимальный элемент: {result}')
sorted_list = sorted(spisok)
result = sorted_list[0]
print(f'Минимальный элемент: {result}')
count1 = 0
count2 = 0
ret = 0
for i in spisok:
    if i > 0:
        count1 += 1
    else:
        count2 += 1
for i in spisok:
    if i % 10 == 0:
        ret += 1
print(f'Колличество положительных чисел: {count1}')
print(f'Колличество отрицательных чисел: {count2}')
print(f'Колличество нулей: {ret}')




