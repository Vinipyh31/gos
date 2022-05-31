#Функция для считывания файла в словарь, r- режим чтения
def file_to_dict(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
        owners = {}
        for record in data:
            info = record.strip().split(': ')
            owner, name = info[0], info[1]
            if not owner in owners:
                owners[owner] = name
        return owners


# Функция для записи словаря в файл, w- режим записи
def dict_to_file(owners, filename):
    #открываем файл 
    with open(filename, 'w', encoding='utf-8') as f:
        for owner, name in owners.items():
            f.write(f'{owner}: {name}\n')

owners_file = 'ЖКХ.txt'
OwnersBook = file_to_dict(owners_file)
# команды
while True:
    command = int(input("""\nМеню:
1. Вывод владельцев
2. Поиск владельца
3. Добавление владельца
4. Переименование владельца
5. Удаление владельца
0. Выход из программы
Введите действие:"""))
    print()
    # проверка какая команда выбрана
    if command == 1:
        print('Вывод владельцев:')
        for number, name in OwnersBook.items():
            #вывод результата
            print(f'Номер квартиры: {number}, Владелец: {name}')
    elif command == 2:
        #поиск, уточнение 
        take = int(input("""Поиск контакта.
Контакт нужно найти по номеру квартиры (1) или по Владельцу (2)?"""))
        if take == 1:
            number = input('Номер квартиры:')
            #проверка есть ли такая квартира в базе
            if number in OwnersBook:
                name = OwnersBook[number]
            #если есть
                print(f'Номер квартиры: {number}, Владелец: {name}')
            else:
                print(f'Квартира не найдена!')
            #поиск по фамилии владельца
        elif take == 2:
            name = input('Владелец:')
            if name in OwnersBook.values():
                number = list(OwnersBook.keys())[list(OwnersBook.values()).index(name)]
                #если есть выводим результат
                print(f'Номер квартиры: {number}, Владелец: {name}')
            else:
                print(f'Владелец не найден!')
        else:
            break
            #Добавление владельца
    elif command == 3:
        print('Добавление владельца:')
        #вод данных
        number = input('Номер квартиры:')
        name = input('Владелец:')
        #запись
        OwnersBook[number] = name
        print(f'Владелец добавлен!')
    elif command == 4:
        print('Переименование владельца:')
        number = input('Номер квартиры:')
        #проверяем, есть ли такая квартира в базе
        if number in OwnersBook:
            name = OwnersBook[number]
            print(f'Номер квартиры: {number}, Владелец: {name}')
            #меняем владельца
            name = input('Введите нового Владельца')
            OwnersBook[number] = name
            print(f'Данные изменены!')
        else:
            print(f'Данные не найдены!')
    elif command == 5:
        print('Удаление владельца:')
        number = input('Номер квартиры:')
        #аналогичная проверка
        if number in OwnersBook:
            print(f'Номер квартиры: {number}, Владелец: {name}')
            #функция удаления
            del (OwnersBook[number])
            print(f'Владелец удалён!')
        else:
            print(f'Данные не найден!')
    else:
        break

    dict_to_file(OwnersBook, owners_file)