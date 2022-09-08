from datetime import datetime

from vadim import create_job, delete_job, print_job, unlog_sys


def login(names):
    ok = False
    print("Добрый день! Необходимо залогиниться")
    print(f"{names}")
    print("Представьтесь, кто Вы?")
    while not ok:
        x = input("Введите число от 1 до 4: ")
        if x in ['1','2','3','4']: #изменил условие правильности ввода
            ok = True
        else:
            print("Вы ошиблись!")
    return x

def inp_date(date):
    d = input("Введите дату: ")


def inp_period(perod):
    ok = False
    print("Выберите период времени")
    print(f"{period}")
    while not ok:
        x = input("Введите число от 1 до 3: ")
        if x in ['1','2','3']: #изменил условие правильности ввода
            ok = True
        else:
            print("Вы ошиблись!")
    return x


def inp_menu(menu):
    ok = False
    print("Что Вы хотите сделать?")
    print(f"{menu}")
    while not ok:
        x = input("Введите число от 1 до 4: ")
        if x in ['1','2','3','4']: #изменил условие правильности ввода
            ok = True
        else:
            print("Вы ошиблись!")
    return x

def inp_txt():
    return input("Опишите суть дела: ")


names = ("1. Константин 2. Лада 3. Вадим 4. Сергей")
menu = ("1. Создать дело 2. Удалить дело 3. Вывести все дела 4. Разлогиниться")
period = ("1. Утро 2. День 3. Вечер")
#Добавил оформление время дня
PIECE_OF_DAY = \
    {
        0: 'Утро',
        1: 'День',
        2: 'Вечер'
    }
name_kode = int(login(names))
while True:
    menu_kode = int(inp_menu(menu))
    match menu_kode:
        case 1:
            date = input("Введите дату в формате 01.01.2000:\n") #добавил перенос на новуя строку
            time_kode = int(inp_period(period))
            text_delo = inp_txt()
            Flag = create_job(name_kode, date, time_kode, text_delo)
            if Flag:
                print("Дело успешно создано")
        case 2:
            date = input("Введите дату в формате 01.01.2000:\n") #добавил перенос на новуя строку
            time_kode = int(inp_period(period))
            Flag1 = delete_job(name_kode, date, time_kode)
            if Flag1:
                print("Дело успешно удалено")
        case 3:
            date = input("Введите дату в формате 01.01.2000:\n") #добавил перенос на новуя строку
            for index, i in enumerate(print_job(name_kode, date)):#Добавил оформление время дня
                print(f'{PIECE_OF_DAY[index]}: {i}')
        case 4:
            unlog_sys(name_kode)
            break