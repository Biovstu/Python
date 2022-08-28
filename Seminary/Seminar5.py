



# lst = []
# for number in range(1, 10):
#     lst.append(number**2)
# print(lst)
# lst2 = [number**2 for number in range(1,10)]

# print(lst2)

# lst = []
# for number in range(1, 10):
#     if number % 2 == 0:
#         lst.append(number**2)
# print(lst)
# lst2 = [number**2 for number in range(1,10) if number % 2 == 0]

# print(lst2)

# lst = []
# for number in range(1, 10):
#     if number % 2 == 0:
#         lst.append(number**2)
#     else:
#         lst.append(number**3)
# print(lst)
# lst2 = [number**2 if number % 2 == 0 else number**3 for number in range(1,10) ]

# print(lst2)

# lst = []
# for number in range(1, 10):
#     if number % 5 != 0:
#         if number % 2 == 0:
#             lst.append(number**2)
#         else:
#             lst.append(number**3)
# print(lst)
# lst2 = [number**2 if number % 2 == 0 else number**3 for number in range(1,10) if number % 5 != 0]

# print(lst2)

# print({item: item*2 for item in range(10)})

# print({item for item in range(10)})

# N, a, b = input().split()

# N = int(N)
# a = int(a)
# b = int(b)

# N, a, b = map(int, input().split())

# N, a, b = map(lambda x: int(x) / 1000, input().split())

# a = map(int, input().split())
# print(*a)

# lst = [1,2,3,4,5,6,7,8,0,1,0,0,2]

# print(*filter(lambda x: True,lst))

# print(*filter(lambda x: x % 2 == 0,lst))

# print(*filter(lambda x: x % 2 != 0,lst))

# print(*filter(lambda x: x,lst))

# lst = list(filter(lambda x: x,lst))
# print(lst)

# a = [1,2,3,4,5,6]
# b = ['a','b','c']
# c = ['qwqer','tyu','gjf','jjgj','gehe','klli']

# for trip in zip(a,b,c):
#     print(trip)

# a = {1,2,3,4,5,6}
# b = ['a','b','c']
# c = ['qwqer','tyu','gjf','jjgj','gehe','klli']

# for trip in zip(a,b,c):
#     print(trip)

# a = {1: 3,2:5,3:6}
# b = ['a','b','c']
# c = ['qwqer','tyu','gjf','jjgj','gehe','klli']

# for trip in zip(a,b,c):
#     print(trip)

# for i, value in enumerate(c):
#     print(i, value)

# def f(n):
#     d = 2
#     lst = []
#     while n != 1:
#         if n % d == 0:
#             lst.append(d)
#             n //= d
#         else:
#             d += 1
#     return lst
# print(f(36))

# tmp = '3x - 2b'.replace(' ', '')


# def a(s):
#     for i, char in enumerate(s):
#         if not char.isdigit():
#             break
#     return int(s[:i]), s[i:]


# def mnog(m, dct):
#     last = -1
#     for i, char in enumerate(m):
#         if char == '+' or char == '-':
#             coef, var = a(m[last + 1:i])
#             dct[var] = coef
#             last = i
#     coef, var = a(m[last + 1:])
#     dct[var] = coef


# dct_ = {}

# mnog(tmp, dct_)

# print(dct_)

'''
2. Дан список чисел. Создайте список, в который попадают числа, описываемые 
   возрастающую последовательность. 
   Порядок элементов менять нельзя.
    
    *Пример:* 
    
    [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
    

3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

'''
# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

# a = '15 16 17 19 20 21 22 23'

# lst = list(map(int, a.split(' ')))

# for i, v in enumerate(lst):
#     if v != lst[i+1]-1:
#         print(v+1)
#         break

# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# a = ' '.join(filter(lambda x: 'абв' not in x,' файле находиабвтся N натуральных чисел, запабвисанных через пробел.'.split()))
# print(a)

# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые 
#    возрастающую последовательность. 
#    Порядок элементов менять нельзя.
    
#     *Пример:* 
    
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# posl = [1, 5, 2, 3, 4, 6, 1, 7]
# for n in range(len(posl)):
#     lst_posl = [posl[n]]
#     for i in range(n+1, len(posl)):
#         if posl[i] > lst_posl[-1]:
#             lst_posl.append(posl[i])
#     print(lst_posl)
