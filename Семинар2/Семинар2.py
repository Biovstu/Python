# print('Hi' * 2) # HiHi
#continue завершает только часть цикла
#break - завершает цикл полностью, при этом не сработает ELSE
#print(dir(a)) выдаст все методы

# def func():
#     print(123)
#     print(456)
#     print(789)
# func()
# func()

# def func(x):
#     print(x ** 2)
# func(5)

# def func(x):
#     return x * x
# itog = func(5)
# print(itog)

# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a,b)

# a = [1,2,3,4]
# #a.append(55)
# a[2] = 'dsfds'
# print(a)
'''
Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
    Для N = 5: 1, -3, 9, -27, 81
'''

# a = int(input('Введите N: '))
# n = 1
# for i in range(a):
#     print(n)
#     n *= -3

'''
Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
'''
# a = input('Введите 1ю строку: ')
# b = input('Введите 2ю строку: ')
# if len(a) >= len(b):
#     i = a.count(b)
# else:
#     i = b.count(a)
# print(f'{"Входит"} - {i} {"раз"}')

# 122233455
# 22

# a = input('Введите 1ю строку: ')
# b = input('Введите 2ю строку: ')
# cnt = 0
# if len(a) >= len(b):
#     for i in range(len(a) - len(b) + 1):
#         if a[i:i + len(b)] == b:
#             cnt += 1    
# else:
#     for i in range(len(b) - len(a) + 1):
#         if b[i:i + len(a)] == a:
#             cnt += 1
# print(f'{"Входит"} - {cnt} {"раз"}')

# import random
# a = random.randrange(-n, n + 1)

# a = 12323.234234235325
# print(round(a, 3))
