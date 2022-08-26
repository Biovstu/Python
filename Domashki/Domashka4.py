#Задача 4.1
#  Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# d = '0.0000001'
# from math import pow, sqrt
# pi = 0
# i = 1
# while abs(1/((2 * i + 1) * pow(-3,i))) >= float(d)/2/sqrt(3):
#     pi += 1/((2 * i + 1) * pow(-3,i))
#     i += 1
# pi = round(2 * sqrt(3) * (1 + pi),11)
# print(str(pi)[:len(d.split('.')[1])+2])

# Задача 4.2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Вариант 1
# def prost(x):
#     for i in range(2,x):
#         if not (x % i):
#             return 0
#             break         
#     else:
#         return 1


# mnoj = []
# for i in range(2, n+1):
#     if prost(i) and n % i == 0:
#         mnoj.append(i)
# print(mnoj)


# Вариант 2: эратосфен
# def eratos(n):
#     sieve = list(range(n + 1))
#     sieve[1] = 0
#     for i in sieve:
#         if i > 1:
#             for j in range(2*i, len(sieve), i):
#                 sieve[j] = 0
#     return sieve


# n = 124
# lst = []
# for i in eratos(n):
#     if i != 0 and n % i == 0:
#         lst.append(i)
# print(lst)


# Задача 4.3
# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# задача 3 через словарь

# chisla = [1,2,3,4,5,6,7,4,5,6,7]
# scet = {}
# for i in chisla:
#     scet[i] = scet.get(i,0) + 1
# chisla.clear()
# for k in scet.keys():
#     if scet[k] == 1:
#         chisla.append(k)
# print(chisla)

# Задача 4.4
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
 
# import random
# k = 5
# key = []
# val = []
# for i in range(k+1):
#     if i == 0:
#         key.append('')
#     elif i == 1:
#         key.append('x')
#     else:
#         key.append('x^'+str(i))
#     val.append(random.randrange(101))
# eq = ''
# for i in range(1,k+2):
#     if val[-i] != 0:
#         if i != k+1:
#             eq += str(val[-i])+'*'+key[-i]+' + '
#         else:
#             eq += str(val[-i])
# eq += ' = 0'
# with open('Domashki\mnogoch.txt', 'w') as f:
#     f.write(eq)

# Задача 4.5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# def sum_mnog(new,m):
#     m = m.replace(' - ',' + -').replace(' = ','*').split(' + ')
#     for i in m:
#         new[i.split('*')[1]] = new.get(i.split('*')[1],0) + int(i.split('*')[0])
#     return new


# with open('Domashki\mnogoch1.txt', 'r') as f:
#     m1 = f.read()

# with open('Domashki\mnogoch2.txt', 'r') as f:
#     m2 = f.read()

# new_mnog = {}
# new_mnog = sum_mnog(sum_mnog(new_mnog,m1),m2)
# s = ''
# for i in new_mnog.keys():
#     if i != '0':
#         if new_mnog[i] > 0:
#             s += ' + '+str(new_mnog[i])+'*'+i
#         elif new_mnog[i] < 0:
#             s += ' - '+str(abs(new_mnog[i]))+'*'+i
#     else:
#         if new_mnog[i] > 0:
#             s += ' + '+str(new_mnog[i])
#         elif new_mnog[i] < 0:
#             s += ' - '+str(abs(new_mnog[i]))

# s = s[3:]+' = 0'

# with open('Domashki\mnogoch.txt', 'w') as f:
#     f.write(s)