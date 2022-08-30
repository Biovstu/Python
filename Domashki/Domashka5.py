# Задача 5.0 (факультативная)
# Дан список чисел. Создайте список, в который попадают числа, описываемые 
# возрастающую последовательность. 
# Порядок элементов менять нельзя.
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# def find_posl(ostatok, base = []):
#     for i in range(len(ostatok)):
#         if len(base) == 0 or ostatok[i] > base[-1]:
#             tmp = base.copy()
#             tmp.append(ostatok[i])
#             if len(tmp) > 1:
#                 print(tmp)
#             if i < len(ostatok) - 1:
#                 find_posl(ostatok[i + 1:], tmp)


# find_posl([1, 5, 2, 3, 4, 6, 1, 7]) #65 возрастающих последовательностей


# Задача 5.1
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
#     Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('Domashki\input51.txt', mode='r', encoding='utf-8') as f:
#     s = f.read()

# print(s)
# a = ' '.join(filter(lambda x: 'абв' not in x, s.split()))
# print(a)

# with open('Domashki\output51.txt', mode='w', encoding='utf-8') as f:
#     f.write(a)

# Задача 5.2
# Создайте программу для игры с конфетами человек против человека.
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#     Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#     Все конфеты оппонента достаются сделавшему последний ход. 
#     Сколько коынфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#     a) Добавьте игру против бота
#     b) Подумайте как наделить бота "интеллектом"

# from random import randrange
# from os import system


# def okonchanie(s):
#     if len(str(s)) > 1 and str(s)[-2] == '1':
#         return ''
#     elif str(s)[-1] in ['0','5','6','7','8','9']:
#         return ''
#     elif str(s)[-1] in ['2','3','4']:
#         return 'ы'
#     else:
#         return('а')


# system('cls')
# n = 58
# print('Правила игры:')
# print(f'На столе лежит {n} конфет{okonchanie(n)}')
# print('Два игрока делают ходы по-очереди.\nЗа один ход можно взять от 1 до 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.')
# input('Для продолжения нажмите ENTER...')
# input('Сейчас пройдет жеребьевка\nДля продолжения нажмите ENTER...')
# hod_bota = randrange(10) % 2
# if not hod_bota:
#     print('Первый ход за ботом')
# else:
#     print('Первый ход за вами')
# input('Для продолжения нажмите ENTER...')
# while n > 0:
#     hod_bota = not hod_bota
#     if hod_bota:
#         if n % 29 == 0:
#             x = randrange(1,29)
#         else:
#             x = n - (n // 29) * 29
#         n -= x
#         print('Бот забрал ',x)
#         print(f'Осталось: {n}, конфет{okonchanie(n)}')
#     else:
#         wrong_input = True
#         while wrong_input:
#             x = input('Сколько конфет вы заберете: ')
#             if n < 28:
#                 n_max = n
#             else:
#                 n_max = 28
#             if x.isdigit() and int(x) >= 1 and int(x) <= n_max:
#                 x = int(x)
#                 wrong_input = False
#             else:
#                 print('Не верно!\nНужно число от 1 до',n_max)
#         n -= x
#         print('Вы забрали ',x)
#         print(f'Осталось: {n}, конфет{okonchanie(n)}')
# if hod_bota:
#     print('Бот забрал все! Жалкий человечишка)))')
# else:
#     print('Ты победил....\nВ этот раз...')

# Задача 5.3
# Создайте программу для игры в "Крестики-нолики".

# осталось добавить защиту от дурака
# def prnt_tablo(tablo):
#     print('+' + '-' * 11 + '+')
#     print('| ' + tablo[0][0] + ' | ' + tablo[0][1] + ' | ' + tablo[0][2] + ' |')
#     print('+' + '-' * 11 + '+')
#     print('| ' + tablo[1][0] + ' | ' + tablo[1][1] + ' | ' + tablo[1][2] + ' |')
#     print('+' + '-' * 11 + '+')
#     print('| ' + tablo[2][0] + ' | ' + tablo[2][1] + ' | ' + tablo[2][2] + ' |')
#     print('+' + '-' * 11 + '+')


# from os import system
# system('cls')

# krest_nol = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
# hod_x = False
# ne_pobeda = True
# hody = []
# while ne_pobeda and len(hody) < 9:
#     system('cls')
#     prnt_tablo(krest_nol)
#     hod_x = not hod_x
#     if hod_x:
#         mask = 'X'
#     else:
#         mask = '0'
#     wrong = True
#     while wrong:
#         strok_stolbec = list(map(lambda x: int(x) - 1, list(input(f'Выберите ячейку для {mask} (строка столбец):\n').split())))
#         if strok_stolbec not in hody:
#             wrong = False
#             hody.append(strok_stolbec)
#         else:
#             print('Такой ход уже был, попробуйте снова...')
#     krest_nol[strok_stolbec[0]][strok_stolbec[1]] = mask
#     if krest_nol[strok_stolbec[0]][0] == mask and krest_nol[strok_stolbec[0]][1] == mask and krest_nol[strok_stolbec[0]][2] == mask:
#         ne_pobeda = False
#     elif krest_nol[0][strok_stolbec[1]] == mask and krest_nol[1][strok_stolbec[1]] == mask and krest_nol[2][strok_stolbec[1]] == mask:
#         ne_pobeda = False
#     elif krest_nol[0][0] == mask and krest_nol[1][1] == mask and krest_nol[2][2] == mask:
#         ne_pobeda = False
#     elif krest_nol[0][2] == mask and krest_nol[1][1] == mask and krest_nol[2][0] == mask:
#         ne_pobeda = False
# system('cls')
# prnt_tablo(krest_nol)
# if len(hody) < 9:
#     print('Победу одержал',mask)
# else:
#     print('Ничья')

# Задача 5.4
# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#     Входные и выходные данные хранятся в отдельных текстовых файлах.

# сжатие
# with open('Domashki/unzip54.txt', 'r') as f:
#     unzipped = f.read()

# print(unzipped)
# zipped = ''
# a = unzipped[0]
# for i in range(1,len(unzipped)):
#     a += unzipped[i]
#     if a[0] != unzipped[i] or i == len(unzipped) - 1 or len(a) == 9:
#         zipped += a[0] + str(len(a))
#         a = unzipped[i]
# print(zipped)

# with open('Domashki/zip54.txt', 'w') as fil:
#     fil.write(zipped)

# восстановление
# with open('Domashki/zip54.txt', 'r') as f:
#     zipped = f.read()

# print(zipped)
# unzipped = ''
# for i in range(0,len(zipped),2):
#     unzipped += zipped[i] * int(zipped[i + 1])
# print(unzipped)

# with open('Domashki/unzip54.txt', 'w') as fil:
#     fil.write(unzipped)