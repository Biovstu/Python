# print('HEllo world')
#a = 123
#b = 1.23
#print(type(a))
#print(type(b))
#s = 'hello world'
#print(s)
#print(type(s))
#print('{1} - {2} - {0}'.format(a,b,s))
#print(f'{a} - {b} - {s}')
#list = ['1','2','3']
#print(list)
#print('Введите a')
#a = int(input())
#print('Введите B')
#b = float(input())
#print(f'{a} + {b} = {a+b}')
#a = 1.345677
#b = 3
#c = round(a * b, 3) # % - остаток деления , // - целая часть
#print(c)
#a = 3
#a *= 5 #сокращенные опрации
#print(a)

#a = 1 < 3 < 5
#print(a)

#func = 1
#T = 4
#x = 2
#print(func<T>(x))

#f = [1,2,3,4]
#print(f)
#print(not 2 in f)

#is_odd = f[0] % 2 == 0
#print(is_odd)

#is_odd = not f[0] % 2 # 0 и 1 воспринимает как логичесие
#print(is_odd)

#a = int(input('a = '))
#b = int(input('b = ')) 
#if a > b:
#    print('Большее ',a)
#else:
#    print('Большее ',b)

#username = input('Введите имя: ')
#if username == 'Марина':
#    print('Привет, Марина')
#elif username == 'Костя':
#    print('Люблю Алёнку')
#else:
#    print('Привет, ', username)

#original = int(input('Введи число '))
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#else:
#    print('Пожалуй хватит')
#print(inverted)

#for i in range(0,100,5):
#    print(i)

#for i in 'qwerty':
#    print(i)

#text = 'съешь еще этих мягких французских булок'

#print(len(text))
#print(text[0])
#print(text[len(text)-1])
#print(text[0:9])
#print(text[0:-9])

#line = ""
#for i in range(5):
#    line = ""
#    for j in range(5):
#        line += "*"
#    print(line)

#text = 'съешь ещё этих мягких французских булок'
#print(len(text))      # 39
#print('ещё' in text)  # True
#print(text.isdigit()) # False
#print(text.islower()) # True
#print(text.replace('ещё','ЕЩЁ')) #
#for c in text:
#    print(c)
#print(text[0:len(text):7])  # сеикакл
#text = text[2:9] + text[-5] + text[:2] # ...
#print(text)

#colors = ['red', 'green', 'blue']
#for e in colors:
#    print(e)  # red green blue
#for e in colors:
#    print(e*2)  # redred greengreen blueblue
#colors.append('gray') # добавить в конец
#print(colors == ['red', 'green', 'blue', 'gray']) # True
#colors.remove('red')
#del colors[0] # удалить элемент
#print(colors)

#def f(x):
#    if x == 1:
#        return 'Целое'
#    elif x == 2.3:
#        return 23
#    else:
#        return

#arg = 7
#print(f(arg))
#print(type(f(arg)))

a = int(input('Введитие a'))
b = int(input('Введитие b'))
if a ** 2 == b:
    print('Да')
else:
    print('Нет')