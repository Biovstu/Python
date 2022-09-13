from data_base import get_data, change_data

# убираем это, и заносим в качестве значения по умолчанию
#a = None

def print_job(x, date, a = None): #добавили значение по-умолчанию
    # global a
    if a is None:
        a = get_data(x)
    return a[date]


def create_job(x, date, time, txt, a = None): #добавили значение по-умолчанию
    if a is None:
        a = get_data(x)
    #a.setdefault
    tmp = a.get(date, ['', '', '']) #Предварительно вытягиваем дела на дату, если такой даты нет, то создаем пустой список
    tmp[time - 1] = txt
    a[date] = tmp
    change_data(x, a) #добавил сохранение
    return True


def delete_job(x, date, time, a = None): #добавили значение по-умолчанию
    if a is None:
        a = get_data(x)
    a[date][time - 1] = ''
    change_data(x, a) #добавил сохранение
    return True


def unlog_sys(x, a = None): #добавили значение по-умолчанию
    if a is None:
        a = get_data(x)
    change_data(x, a)#добавил пропущенный логин
    a = None
    return True