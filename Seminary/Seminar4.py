# a = [1, 2, 3]
# print(id(a))

# a = 5
# b = a
# print(a is b)

# a = 55
# b = 55
# print(a is b)

# если None true false, то лучше испольщовать is
# не путать оператор логический и оператор логический побитовый

# from second import func
# func()

# import second
# second.func()

# form second import func as os
# os()

# from second import * # Так не делать

# f = open('123.txt') #rt - по умолчанию
# print(f.read())

# f = open('123.txt','a')
# f.write('cccccccc\n')
# f.close()

# with open('123.txt', 'a') as f:
#     f.write('ffgggg\n')

# with open('123.txt', 'r') as f, open('333.txt','w') as f1:
#     f1.write(f.read())

# read - читает все одну строку
# readline - берет только одну строку, а из файла ее забирает
# readlines - список всех строк

'''
1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
В качестве символа-разделителя используйте пробел.
'''
# def func(chisla):
#     a = chisla.split() #разделят по непечатным симолвам
#     a_min = float('inf')
#     a_max = float('-inf')
#     for i in a:
#         if int(i) > a_max:
#             a_max = int(i)
#         if int(i) < a_min:
#             a_min = int(i)
#     return a_max, a_min


# print(func('7 2 3 14 1  6'))

'''
2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
    1) с помощью математических формул нахождения корней квадратного уравнения
    
    2) с помощью дополнительных библиотек Python

    D = b * b - 4 * a * c
x = (-b +- D**0.5) / (2 * a)

'''
#вариант 1
# def kv_ur(a, b, c):
#     D = b * b - 4 * a * c
#     return ((-b + D**0.5) / (2 * a)), ((-b - D**0.5) / (2 * a))

# print(kv_ur(1, -3, 2))

# вариан2

# import math
# def kv_ur(a, b, c):
#     D = math.pow(b, 2) - 4 * a * c
#     return ((-b + math.sqrt(D)) / (2 * a)), ((-b - math.sqrt(D)) / (2 * a))

# print(kv_ur(1, -3, 2))

# from math import pow, sqrt
# def kv_ur(a, b, c):
#     D = pow(b, 2) - 4 * a * c
#     return ((-b + sqrt(D)) / (2 * a)), ((-b - sqrt(D)) / (2 * a))

# print(kv_ur(1, -3, 2))

'''
3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное)
этих двух чисел.
'''
# from math import gcd
# def nok(a, b):
#     return abs(a * b) / gcd(a, b)


# print(nok(7, 2))

# def gcd(a, b):
#     if a == b:
#         return a
#     if a > b:
#         return gcd(b, a - b)
#     return gcd(a, b - a)


# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# print(gcd(35, 25))

#''.join(s) # - склеить строку из списка