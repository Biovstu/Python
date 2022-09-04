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


zap_knig = upload('domashki\\basa_kontantov.txt')#чтение из базы
show_spis(zap_knig)# вывод книжки

print('----added----')
zap_knig.extend(upload('domashki\\istochnik.txt'))#добавлениие из внешнего файла
show_spis(zap_knig)# вывод книжки


form = int(input('Выберите формат записи\n0 - в дереве\n1 - в строке\n'))
download('domashki\\priemnik.txt', form, zap_knig)#сохранение во внешний файл

