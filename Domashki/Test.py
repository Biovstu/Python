TEL_BASE_PATH = 'C:\\Users\\gehor\\Documents\\BI\\PyCharm\\Domashka9\\tel_base\\'


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


#вывод списка
def show_spis(spis):
    exp_spis = []
    derevo = \
        {
            0: 'Фамилия',
            1: 'Имя',
            2: 'Телефон',
            3: 'Описание'
        }
    for index, i in enumerate(spis):
        exp_spis.append('#' + str(index + 1))
        for jindex, j in enumerate(i):
            spis += str(derevo[jindex]) + ': ' + str(j) + '\n'
    return exp_spis


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


file_name = TEL_BASE_PATH + '966221933' + '.txt'

tmp = upload(file_name)
zapros = 'Кутовой,Константин,12345,ЭтоЯ'.split(',')
print(zapros)
tmp.append(zapros)
print(tmp)
download(file_name, 1, tmp)
# print(show_spis(upload(file_name)))
