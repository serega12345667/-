# '''''''''''''''''''''1'''''''''''''''''''''
# books = {}
# count = '1'
#
#
# def add_new_book(num: str = '0') -> None:
#     books[num] = {}
#     author = input('Введите имя автора: ')
#     books[num]['author'] = author
#     naming = input('Введите название книги: ')
#     books[num]['naming'] = naming
#     year = input('Введите год выпуска: ')
#     books[num]['year_of_publish'] = year
#
# add_new_book(count)


# '''''''''''''''''''''2'''''''''''''''''''''
# books = {}
# set_of_keys = {'author', 'naming', 'year_of_publish'}
# count = '1'
#
#
# def add_new_book(num: str = '0') -> None:
#     books[num] = {}
#     for key in set_of_keys:
#         books[num][key] = input(f'Введите {key}: ')
#
#
# add_new_book(count)
# print(books)
#
#
# # '''''''''''''''''''''3'''''''''''''''''''''
# books = {}
# map_of_keys = {'Автор': 'имя автора', 'Название': 'название произведения', 'Год выпуска': 'год выпуска'}
# count = '1'
#
#
# def add_new_book(num: str = '0') -> None:
#     books[num] = {}
#     for key in map_of_keys.keys():
#         books[num][key] = input(f'Введите {map_of_keys[key]}: ')
#
# add_new_book(count)
# print(books)

with open(file='file_1.txt', mode='r', encoding='UTF-8') as f:
    full_text = f.read().split()
    with open(file='ban_words.txt', mode='r', encoding='UTF-8') as ban:
        ban_words = ban.read().split()
        with open(file='new.txt', mode='w', encoding='UTF-8') as new:
            result = ''
            for word in full_text:
                if word.lower() not in ban_words:
                    result += f'{word} '
            result = result[:-1]
            new.write(result)

# .lower() / .upper() - функции для управления регистром символов в строке


# dic = {'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', 'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b',
#        'В': 'V', 'в': 'v', 'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E',
#        'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh', 'З': 'Z', 'з': 'z',
#        'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
#        'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p',
#        'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u',
#        'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh', 'Ц': 'Tc', 'ц': 'tc', 'Ч': 'Ch',
#        'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ы': 'Y', 'ы': 'y',
#        'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia'}
#
#
# with open(file='start.txt', mode='r', encoding='UTF-8') as f_1:
#     words_start = list(f_1.read())
#     with open(file='results.txt', mode='w', encoding='UTF-8') as f_2:
#         for i in words_start:
#             f_2.write(f'{dic.get(i, i)}')
#
# diction = dict(a='1', b='2', c='3')
# print(diction.get('d', 'Такого ключа нет'))


# output_file = open(file='results.txt', mode='w', encoding='UTF-8')
# while True:
#     filename = input('Введите название файла для считывания, иначе quit: ')
#     if filename == 'quit':
#         break
#     try:
#         current_file = open(file=filename, mode='r', encoding='UTF-8')
#     except FileNotFoundError:
#         print('There is no file you entered. Try another')
#         continue
#     output_file.write(current_file.read() + '\n')
#     current_file.close()
# output_file.close()

# data_files = []
# while True:
#     filename = input('Введите название файла для считывания, иначе quit: ')
#     if filename == 'quit':
#         break
#     try:
#         current_file = open(file=filename, mode='r', encoding='UTF-8')
#     except FileNotFoundError:
#         print('There is no file you entered. Try another')
#         continue
#     data_files.append(set(current_file.read()))
#     current_file.close()
#
# result = ''
# ----------1 решение-----------
# one_file = data_files.pop()
# for symbol in one_file:
#     in_all = True
#     for file in data_files:
#         if symbol not in file:
#             in_all = False
#     if in_all:
#         result += symbol + ' '

# ----------2 решение-----------
# resulting_set = data_files.pop()
# for file in data_files:
#     resulting_set = resulting_set.intersection(file)



# with open(file='results.txt', mode='w', encoding='UTF-8') as f:
#     f.write(' '.join(resulting_set))
