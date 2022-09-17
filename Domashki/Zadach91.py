# Задача 5.3
# Создайте программу для игры в "Крестики-нолики".

# осталось добавить защиту от дурака
def prnt_tablo(tablo):
    print('+' + '-' * 14 + '+')
    print('| ' + tablo[0][0] + ' | ' + tablo[0][1] + ' | ' + tablo[0][2] + ' |')
    print('+' + '-' * 14 + '+')
    print('| ' + tablo[1][0] + ' | ' + tablo[1][1] + ' | ' + tablo[1][2] + ' |')
    print('+' + '-' * 14 + '+')
    print('| ' + tablo[2][0] + ' | ' + tablo[2][1] + ' | ' + tablo[2][2] + ' |')
    print('+' + '-' * 14 + '+')


from os import system
from random import randrange
from progress.bar import Bar
import time
import emoji

krest_nol = [['  ','  ','  '],['  ','  ','  '],['  ','  ','  ']]

system('cls')
print('Проведем жеребевку первого хода')
bar = Bar('Жеребьевка', max=10)
for i in range(10):
    time.sleep(1)
    bar.next()
bar.finish()
hod_x = randrange(10) % 2
if not hod_x:
    print(emoji.emojize('Первые ходят :cross_mark: '))
else:
    print(emoji.emojize('Первые ходят :hollow_red_circle: '))
input('Для продолжения нажмите ENTER...')
system('cls')

ne_pobeda = True
hody = []
while ne_pobeda and len(hody) < 9:
    system('cls')
    prnt_tablo(krest_nol)
    hod_x = not hod_x
    if hod_x:
        mask = emoji.emojize(':cross_mark:')
    else:
        mask = emoji.emojize(':hollow_red_circle:')
    wrong = True
    while wrong:
        strok_stolbec = list(map(lambda x: int(x) - 1, list(input(f'Выберите ячейку для {mask} (строка столбец):\n').split())))
        if strok_stolbec not in hody:
            wrong = False
            hody.append(strok_stolbec)
        else:
            print('Такой ход уже был, попробуйте снова...')
    krest_nol[strok_stolbec[0]][strok_stolbec[1]] = mask
    if krest_nol[strok_stolbec[0]][0] == mask and krest_nol[strok_stolbec[0]][1] == mask and krest_nol[strok_stolbec[0]][2] == mask:
        ne_pobeda = False
    elif krest_nol[0][strok_stolbec[1]] == mask and krest_nol[1][strok_stolbec[1]] == mask and krest_nol[2][strok_stolbec[1]] == mask:
        ne_pobeda = False
    elif krest_nol[0][0] == mask and krest_nol[1][1] == mask and krest_nol[2][2] == mask:
        ne_pobeda = False
    elif krest_nol[0][2] == mask and krest_nol[1][1] == mask and krest_nol[2][0] == mask:
        ne_pobeda = False
system('cls')
prnt_tablo(krest_nol)
if len(hody) < 9:
    print('Победу одержал',mask)
    print(emoji.emojize(':fireworks:'))
else:
    print(emoji.emojize('Ничья :clapping_hands: '))