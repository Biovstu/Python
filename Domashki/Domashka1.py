# Задача 1.1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# a = int(input('Введите номер дня недели: '))
# if a in range(1,6):
#     print('Нет')
# else:
#     if a in range(6,8):
#         print('Да')
#     else:
#         print('Введите число от 1 до 7')

# Задача 1.2
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# 
# print('x', 'y', 'z', '¬(X ⋁ Y ⋁ Z)','¬X ⋀ ¬Y ⋀ ¬Z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(f'{x} {y} {z}      {not (x or y or z)}      {not x and not y and not z}')

# Задача 1.3
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите координату X: '))
# y = int(input('Введите координату Y: '))
# if x == 0 and y == 0:
#     print('Лежит в начале координат')
# elif x == 0 and y != 0:
#     print('Лежит на оси 0Y')
# elif x != 0 and y == 0:
#     print('Лежит на оси 0X')
# elif x > 0:
#     if y > 0:
#         print('1я четверть')
#     else:
#         print('4я четверть')
# else:
#     if y > 0:
#         print('2я четверть')
#     else:
#         print('3я четверть')
 
# Задача 1.4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).
# РЕшение 1
a = int(input('Введите номер четверти: '))
c = ['номер четверти от 1 до 4','x > 0 and y > 0','x < 0 and y > 0','x < 0 and y < 0','x > 0 and y < 0']
if a in range(1,5):
    print(c[a])
else:
    print(c[0])
#решение 2
# if a in range(1,5):
#     if a == 1:
#         print('x > 0 and y > 0')
#     elif a == 2:
#         print('x < 0 and y > 0')
#     elif a == 3:
#         print('x < 0 and y < 0')
#     else:
#         print('x > 0 and y < 0')
# else:
#     print('номер четверти от 1 до 4')

# Задача 1.5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# a_xy = input('Введите координаты точки A в формате "x,y": ')
# b_xy = input('Введите координаты точки B в формате "x,y": ')
# a_x = int(a_xy.split(',')[0])
# a_y = int(a_xy.split(',')[1])
# # print(a_x)
# # print(a_y)
# b_x = int(b_xy.split(',')[0])
# b_y = int(b_xy.split(',')[1])
# # print(b_x)
# # print(b_y)
# print('Расстояние между точками = ', ((a_x - b_x) ** 2 + (a_y - b_y) ** 2) ** 0.5)