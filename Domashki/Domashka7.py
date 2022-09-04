'''
Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. 
- *под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, 
   пустая строка - разделитель*
    
    *Фамилия_1*
    *Имя_1*
    *Телефон_1*
    *Описание_1*
    
    *Фамилия_2*
    *Имя_2*
    *Телефон_2*
    *Описание_2*
    
    *и т.д.в файле на одной строке хранится все записи, символ разделитель - **;***
    
    *Фамилия_1,Имя_1,Телефон_1,Описание_1*
    *Фамилия_2,Имя_2,Телефон_2,Описание_2*
    
    *и т.д.*
Фамилия_1
Имя_1
Телефон_1
Описание_1

Фамилия_2
Имя_2
Телефон_2
Описание_2

'''


#чтение из файла
def upload(file_name):
    zap_tmp = []
    with open(file_name, mode='r', encoding='utf-8') as data:
        for line in data:
            zap_tmp.append(line.replace('\n', ''))
    zap_knig = []
    if '' in zap_tmp:
        empty_str = -1
        zap_tmp.append('')
        for index, i in enumerate(zap_tmp):
            if i == '':
                zap_knig.append(zap_tmp[empty_str+1:index])
                empty_str = index
    else:
        for zap in zap_tmp:
            zap_knig.append(zap.split(','))
    return zap_knig


# вывод книжки
def show_spis(spis):
    derevo = \
        {
            0: 'Фамилия',
            1: 'Имя',
            2: 'Телефон',
            3: 'Описание'
        }
    for index, i in enumerate(spis):
        print('Запись', index + 1)
        for jindex, j in enumerate(i):
            print(f'{derevo[jindex]}: {j}')


#сохранение в файл
def download(file_name, format_zapisi, knigka):
    with open(file_name, mode='w', encoding='utf-8') as data:
        if format_zapisi:
            for index, i in enumerate(knigka):
                if index < len(knigka) - 1:
                    data.write(f'{",".join(i)}\n')
                else:
                    data.write(f'{",".join(i)}')
        else:
            for index, i in enumerate(knigka):
                for jindex, j in enumerate(i):
                    # data.write(f'{j}\n')
                    if jindex == len(i) - 1 and index == len(knigka) - 1:
                        data.write(f'{j}')
                    else:
                        data.write(f'{j}\n')
                if index < len(knigka) - 1:
                    data.write('\n')


from os import system

zap_knig = upload('domashki\\basa_kontantov.txt')#чтение из базы
vyhod = False
while not vyhod:
    system('cls')
    print('Добро пожаловать в записную книжку\nИмеется записей:', len(zap_knig))
    print('Выберите пункт меню:')
    print('1. Показать все записи')
    print('2. Добавить из файла')
    print('3. Экспортировать в файл')
    print('4. Поиск по записям')
    print('0. Выход')
    tmp = []
    vybor = int(input())
    match vybor:
        case 1:
            system('cls')
            show_spis(zap_knig)# вывод книжки
            input('Для возвращения в меню нажмите ENTER...')
        case 2:
            system('cls')
            file = input('Введите путь к файлу:\n')
            tmp.extend(upload(file))
            print('Будут загружены следующие записи:')
            show_spis(tmp)
            y = input('Для подтверждения загрузки введите Y/y:')
            if y in ['Y', 'y']:
                zap_knig.extend(tmp)
        case 3:
            system('cls')
            form = int(input('Выберите формат записи\n0 - в дереве\n1 - в строке\n'))
            file = input('Введите путь к файлу:\n')
            download(file, form, zap_knig)#сохранение во внешний файл
        case 4:
            system('cls')
            zapros = input('Введите поисковый запрос\n')
            tmp = [i for i in zap_knig if zapros in i[0] or zapros in i[1]]
            print(f'Найденно {len(tmp)} записей')
            show_spis(tmp)
            input('Для возвращения в меню нажмите ENTER...')
        case 0:
            system('cls')
            y = input('Для подтверждения входа введите Y/y:')
            if y in ['Y', 'y']:
                vyhod = True
download('domashki\\basa_kontantov.txt', 1, zap_knig)