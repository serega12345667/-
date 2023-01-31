Great_basketball_players = {'Иванов': 190}

command = input('Введите команду (add-добавить)/(delete-удалить)/(find-отобразить)/(replace-заменить)/(exit-выйти)): ')
while True:
    if command == 'add' or command == 'replace':
        name = input('Введите ФИО: ')
        name_1 = int(input('Введите рост: '))
        Great_basketball_players[name] = name_1
        print(Great_basketball_players)
        if command == 'add':
            print('ФИО и рост успешно добавленны')
        else:
            print('Рост успешно изменён')
    elif command == 'delete':
        name = input('Введите ФИО баскетболиста, которое вы хотите удалить: ')
        if name in Great_basketball_players:
            del Great_basketball_players[name]
            print('Данные успешно удалены!')
        else:
            print('Такого ФИО нет!!')
        print(Great_basketball_players)
    elif command == 'find':
        name = input('Введите ФИО: ')
        print(f'Фамилия баскетболиста {name}, его рост: {Great_basketball_players.get(name)} см!')
    elif command == 'exit':
        print('Пока пока ; )')
        break
    else:
        print('Введите допустимую команду!')

    command = input('Введите новую команду (add/delete/find/replace/exit): ')





Book_collection = {'Книга 1': {'author': 'Лабковский', 'title_book': 'Хочу и буду',
'genre': 'Психология', 'year_of_release': 2010, 'number_of_pages': 336, 'publishing_house': 'ЭКСМО'}}
print(Book_collection)

command = input('Введите команду (add-добавить)/(delete-удалить)/(find-отобразить)/(replace-заменить)/(exit-выйти)): ')
while True:
    if command == 'add' or command == 'replace':
        number = input('Введите номер книги: ')
        Book_collection[number] = {}
        author_1 = input('Введите автора книги: ')
        Book_collection[number]['author'] = author_1
        title_book_1 = input('Введите название книги: ')
        Book_collection[number]['title_book'] = title_book_1
        genre_1 = input('Введите жанар книги: ')
        Book_collection[number]['genre'] = genre_1
        year_of_release_1 = input('Введите год выпуска книги: ')
        Book_collection[number]['year_of_release'] = year_of_release_1
        number_of_pages_1 = input('Введите колличество страниц книги: ')
        Book_collection[number]['number_of_pages'] = number_of_pages_1
        publishing_house_1 = input('Введите издательство книги: ')
        Book_collection[number]['publishing_house'] = publishing_house_1
        print(Book_collection)
        if command == 'add':
            print('Книга успешно добавленна!')
        else:
            print('Данные книги изменены!')
    elif command == 'delete':
        name_0 = input('Вы хотите удалить всю книгу? ')
        if name_0 == 'да':
            name = input('Введите номер книги, которую вы хотите удалить: ')
            if name in Book_collection:
                del Book_collection[name]
                print('Книга успешно удалена!')
            else:
                print('Такой книги нет!')
        elif name_0 == 'нет':
            name = input('Введите номер книги, в которой вы хотите изменить параметры: ')
            name_1 = input('Введите параметр который вы хотите удалить: ')
            if name in Book_collection:
                del Book_collection[name][name_1]
                print('Параметр успешно удален!')
            else:
                print('Такого параметра нет!')
        else:
            print('Такая команда отсутсвует, введите команду: да/нет.')
        print(Book_collection)
    elif command == 'find':
        name = input('Введите номер книги, по которой вы желаете увидить все данные: ')
        print(f'Порядковый номер: {name},\n'
              f'Автор: {Book_collection.get(name).get("author", "-")},\n'
              f'Название книги: {Book_collection.get(name).get("title_book", "-")},\n'
              f'Жанр: {Book_collection.get(name).get("genre", "-")},\n'
              f'Год выпуска: {Book_collection.get(name).get("year_of_release", "-")},\n'
              f'Колличество страниц: {Book_collection.get(name).get("number_of_pages", "-")},\n'
              f'Издатель: {Book_collection.get(name).get("publishing_house", "-")},')
    elif command == 'exit':
        print('Благодарим Вас за работу в нашей программе, всего доброго ; )')
        break
    else:
        print('Введите допустимую команду!')

    command = input('Введите команду (add-добавить)/(delete-удалить)/(find-отобразить)/(replace-заменить)/(exit-выйти)): ')
