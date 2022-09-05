# for number in map(lambda x: x**2, range(10)):
#     print(number)

# for number in filter(lambda x: x % 5 == 0, range(100)):
#     print(number)

# a = filter(lambda x: x % 5 == 0, range(100))

# print(len(a))

# print('----1----')

# for n in a:
#     print(n)

# print('----2----')# второй раз не прочитает

# for n in a:
#     print(n)

# b = next(a)
# c = next(a)
# print('--', b)
# print('--', c)
# for n in a:
#     print(n)

# итератор - это функция
# def f():
#     for n in range(10):
#         return n #полностью выходим из функции

# print(f())

# def f():
#     for n in range(10):
#         yield n #полностью выходим из функции

# a = f()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))# тут ошшибка, так как все закончилось
# print(next(a))
# print(next(a))
# print(next(a))

# print('--1--')

# for item in a:
#     print(item)

# print('--2--')

# for item in a:
#     print(item)

# def my_range(start, stop, step=1):
#     while start < stop:
#         yield start
#         start += step

# for n in my_range(3, 21, 3):
#     print(n)


# def my_range(start, stop=None, step=1):# обычный Рэндж
#     if stop is None:
#         stop = start
#         start = 0
#     while start < stop:
#         yield start
#         start += step


# i = 0#обычный рэндж такое не пустит
# for n in my_range(5, 10, -2):
#     print(n)
#     i += 1
#     if i == 20:
#         break

'''
1. Напишите программу вычисления арифметического выражения заданного строкой.
   Используйте операции +,-,/,*. приоритет операций стандартный.
    *Пример:*
    2+2 => 4;
    1+2*3 => 7;
    1-2*3 => -5;
2. - Добавьте возможность использования скобок, меняющих приоритет операций.
    *Пример:*
    1+2*3 => 7;
    (1+2)*3 => 9;
'''
# 1. Напишите программу вычисления арифметического выражения заданного строкой.
#    Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;


# def scitalka(vyrag):
#     nums = []
#     koef = 1
#     propusk = False
#     for i in range(len(vyrag)):
#         if propusk:
#             propusk = False
#             continue
#         if vyrag[i].isdigit():
#             nums.append(int(vyrag[i]) * koef)
#         elif vyrag[i] == '-':
#             koef = -1
#         elif vyrag[i] == '+':
#             koef = 1
#         elif vyrag[i] == '*':
#             nums[-1] *= int(vyrag[i+1])
#             propusk = True
#         elif vyrag[i] == '/':
#             nums[-1] /= int(vyrag[i+1])
#             propusk = True
#     return sum(nums)
    

def obrabotka(vyrag):
    vyrag = vyrag.replace(' ', '')
    spisok_vyrag = []
    chisla = []
    propusk = False
    pr = None
    for index, i in enumerate(vyrag):
        if pr and index <= pr:
            continue
        elif pr and index == pr + 1:
            spisok_vyrag.append(i)
            continue
        if i.isdigit():
            chisla.append(i)
        elif i == '(':
            pr = vyrag.rfind(')')
            spisok_vyrag.append(str(obrabotka(vyrag[index + 1 : pr])))
        else:
            spisok_vyrag.append(''.join(chisla))
            spisok_vyrag.append(i)
            chisla.clear()
    spisok_vyrag.append(''.join(chisla))
    print(spisok_vyrag)
    return scitalka(spisok_vyrag)

print(obrabotka('(11*(1+3)+2)*8/4'))
