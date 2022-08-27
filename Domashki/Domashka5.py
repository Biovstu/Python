# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#     Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('Domashki\input51.txt', mode='r', encoding='utf-8') as f:
#     s = f.read()

# print(s)
# a = ' '.join(filter(lambda x: 'абв' not in x, s.split()))
# print(a)

# with open('Domashki\output51.txt', mode='w', encoding='utf-8') as f:
#     f.write(a)

# 2. Создайте программу для игры с конфетами человек против человека.

#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#     Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#     Все конфеты оппонента достаются сделавшему последний ход. 
#     Сколько коынфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#     a) Добавьте игру против бота

#     b) Подумайте как наделить бота "интеллектом"

# 3. Создайте программу для игры в "Крестики-нолики".

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#     Входные и выходные данные хранятся в отдельных текстовых файлах.

# сжатие
# with open('Domashki/unzip54.txt', 'r') as f:
#     unzipped = f.read()

# print(unzipped)
# zipped = ''
# a = unzipped[0]
# for i in range(1,len(unzipped)):
#     if a[0] != unzipped[i] or i == len(unzipped) - 1:
#         zipped += a[0] + str(len(a))
#         a = unzipped[i]
#     else:
#         a += unzipped[i]
# print(zipped)

# with open('Domashki/zip54.txt', 'w') as fil:
#     fil.write(zipped)

# восстановление
with open('Domashki/zip54.txt', 'r') as f:
    zipped = f.read()

print(zipped)
unzipped = ''
for i in range(0,len(zipped),2):
    unzipped += zipped[i] * int(zipped[i + 1])
print(unzipped)

with open('Domashki/unzip54.txt', 'w') as fil:
    fil.write(unzipped)