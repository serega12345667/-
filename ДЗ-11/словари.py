# spisok = [5, 1, 6, 2, 8, 3, 6, 2]
#
# for i in range(len(spisok)):
#     f = 0
#     for j in range(0, len(spisok) - i - 1):
#         if spisok[j] > spisok[j + 1]:
#             spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]
#             f = 1
#     if f == 0:
#         break
# print(spisok)

# from random import randint
#
# my_tuple = tuple(randint(1, 200) for i in range(10))
# one_digit_count = two_digit_count = three_digit_count = 0
#
# for el in my_tuple:
#     if el < 10:
#         one_digit_count += 1
#     elif el < 100:
#         two_digit_count += 1
#     else:
#         three_digit_count += 1
#
# print(my_tuple)
# print('Элементов с одной цифрой:', one_digit_count)
# print('Элементов с двумя цифрами:', two_digit_count)
# print('Элементов с тремя цифрами:', three_digit_count)

# my_dict = {'Кирилл': 'Михеев', 1: 0}
# my_dict1 = {}
#
# print(type(my_dict), my_dict)
# print(type(my_dict1))
# Ключом словаря могут быть только неизменямые типы данных
# Неизменяемые типы: число, строка, кортеж
# Все остальные - изменяемые

# my_dict = {1: 2, 3: 4, 5: 6}
#
# my_dict[10] = 0
# print(my_dict)
# del my_dict[10]
# print(my_dict)

# my_dict = dict([(1, 2), (3, 4), (5, 6)])
# print(my_dict)

my_dict = {1: 2, 3: 4, 5: 6}
# .keys() возвращает список всех ключей словаря
# print(type(my_dict.keys()))
# for key in my_dict.keys():
#     print(key)
#
# .values() возвращает список всех значений словаря
# print(type(my_dict.values()))
# for value in my_dict.values():
#     print(value)
#
# .items() возвращает список всех пар словаря
# print(my_dict.items())
# for key, value in my_dict.items():
#     print(key, value)

# Распаковка
# spisok = (1, 2)
# number1, number2 = spisok
# print(number1, number2)

# my_dict = {1: 2, 3: 4, 5: 6}
# my_dict.setdefault(10)
# print(my_dict[10])

# my_dict = {1: 2, 3: 4, 5: 6, 7: 8}
# print(my_dict.popitem())
# print(my_dict)

# my_dict = {1: 2, 3: 4, 5: 6}
# my_dict.update({7: 8, 9: 10})
# print(my_dict)

# Пример нейминга словарей
# names_to_phonenumbers = {'Егор': '+795351512252'}
#
# my_dict = {1: 2, 3: 4, 5: 6, 7: 8}
# result = 1
# for num in my_dict.values():
#     result *= num
# print(result)

# sp = {}
# for i in range(1, 5):
#     a = input('Введите название продукта: ')
#     sp[i] = a
#
# print(sp)
#
# del sp[int(input('Введите номер удаляемого элемента: '))]
#
# print(sp)


# my_dict = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_dict = {}
#
# new_dict['name'] = my_dict.pop('name')
# new_dict['salary'] = my_dict.pop('salary')
# print(my_dict)
# print(new_dict)

# my_dict = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_dict = {}
# new_dict.update(dict([my_dict.popitem()]))
# print(new_dict)
#
#
# def key_by_value(value, diction):
#     for key in diction.keys():
#         if diction[key] == value:
#             return key
#     return 'There is no such key with value you asked'
#
#
# print(key_by_value(value=8000, diction=my_dict))

# numbers = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# my_dict = {numbers[0]: numbers[1:4],
#            numbers[4]: numbers[5:7],
#            numbers[7]: numbers[8:11],
#            numbers[11]: numbers[12:]}
# print(my_dict)
#
# new_dict = {}
# for i in range(len(numbers)):
#     if isinstance(numbers[i], str):
#         for j in range(i + 1, len(numbers)):
#             if isinstance(numbers[j], str):
#                 break
#             if j == len(numbers) - 1:
#                 j += 1
#         new_dict[numbers[i]] = numbers[i + 1:j]
# print(new_dict)

countries_to_capitals = {'Russia': 'Moscow'}

command = input('Enter a command(add/delete/find/replace/exit): ')
while True:
    if command == 'add' or command == 'replace':
        country = input('Enter country name: ')
        capital = input('Enter the name of its capital: ')
        countries_to_capitals[country] = capital
        if command == 'add':
            print('Country and Capital added successfully')
        else:
            print('Capital of a Country changed successfully')
    elif command == 'delete':
        country = input('Enter country name you want to delete: ')
        if country in countries_to_capitals:
            del countries_to_capitals[country]
            print('Country and Capital deleted successfully')
        else:
            print('There is no such country!!')
    elif command == 'find':
        country = input('Enter country name: ')
        print(f'The capital of {country} is {countries_to_capitals.get(country, "unknown")}')
    elif command == 'exit':
        print('Bye Bye')
        break
    else:
        print('Enter valid command!')

    command = input('Enter a command(add/delete/find/replace/exit): ')
