from random import randint
spisok_1 = [randint(-50, 50)
            for i in range(10)]
from random import randint
spisok_2 = [randint(-50, 50)
            for i in range(10)]
spisok_3 = spisok_2 + spisok_1
spisok_3.sort()
print(f'Cписок, содержащий элементы обоих списков: {spisok_3}')


spisok_4 = []
set_spisok_1 = set(spisok_1)
for i in spisok_2:
    if i not in set_spisok_1:
        spisok_4.append(i)
spisok_4 += spisok_1
print(f'Элементы обоих списков без повторений: {spisok_4}')


spisok_5 = []
set_spisok_1 = set(spisok_1)
for i in spisok_2:
    if i in set_spisok_1:
        spisok_5.append(i)
print(f'Элементы общие для двух списков: {spisok_5}')


spisok_6 = []
for spisok in spisok_1:
    if spisok not in spisok_6:
        spisok_6.append(spisok)
for spisok in spisok_2:
    if spisok not in spisok_6:
        spisok_6.append(spisok)
print(f'Уникальные элементы каждого из списков: {spisok_6}')


spisok_7 = []
sorted_list_1 = sorted(spisok_1)
result_1 = sorted_list_1[-1]
result_2 = sorted_list_1[0]
sorted_list_2 = sorted(spisok_2)
result_3 = sorted_list_2[-1]
result_4 = sorted_list_2[0]
spisok_7.append(result_1)
spisok_7.append(result_2)
spisok_7.append(result_3)
spisok_7.append(result_4)
print(f'Максимальное и минимальное значение списов: {spisok_7}')


s = input('Введите строку: ')
s = s.split()
s = ''.join(s)
print(s)
if s == s[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")


spisok_3 = []
spisok = str(input('Введите текст: ')).split(' ')
print(spisok)
spisok_1 = str(input('Введите зарезервированные слова: ')).split(' ')
spisok_2 = []
set_spisok = set(spisok)
for i in spisok_1:
    if i in set_spisok:
        new = i.capitalize()
        spisok_3.append(new)
        print(spisok_3)
j = " ".join(spisok)
print(j)
# Не придумал как вставить слова в текст


a = input('Введите текст: ')
count_digit = 0
count_digit_1 = 0
count_digit_2 = 0
count_digit_3 = 0
for i in a:
    if i == '.':
        count_digit_1 += 1
    if i == '!':
        count_digit_2 += 1
    if i == '?':
        count_digit_3 += 1
count_digit = count_digit_1 + count_digit_2 + count_digit_3
print(f'Количество предложений: {count_digit}')

