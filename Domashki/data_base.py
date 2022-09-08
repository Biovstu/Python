# 1. Константин
# 2. Лада
# 3. Вадим
# 4. Сергей
# dic = {'data': [0,1,2]}

DIC_LOGIN = \
    {
        1:('Konstantin', 'Domashki\\konstatin.txt'),
        2:('Lada', 'Domashki\\lada.txt'),
        3:('Vadim', 'Domashki\\vadim.txt'),
        4:('Sergey', 'Domashki\\sergey.txt')
    }


def get_data(login):
    readed_data = []
    with open(DIC_LOGIN[login][1], mode='r', encoding='utf-8') as data:
        for line in data:
            readed_data.append(line.replace('\n', ''))
    data = list(map(lambda d: d.split('|'), readed_data))
    down_data = {}
    for i in data:
        down_data[i[0]] = i[1:]
    return down_data


def change_data(login, dict_data):
    uploaded_list = [f'{key}|{"|".join(dict_data[key])}' for key in dict_data]
    uploaded_str = '\n'.join(uploaded_list)
    with open(DIC_LOGIN[login][1], mode='w', encoding='utf-8') as data:
        data.write(uploaded_str)
    return True