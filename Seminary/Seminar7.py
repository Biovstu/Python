# модуль проверки корректности
def check(vhod):
    new_chislo = []
    vhod = vhod.replace(',','.').replace(' ','') #заменяем на точки и убиарем пробелы
    koef = ''
    tochka = 0
    tire = 0
    for i in vhod:
        if i == '-':
            if tire:
                return None
            koef = '-'
            tire += 1
        elif i.isdigit():
            new_chislo.append(koef + i)
            if koef == '-':
                koef = ''
        elif i == '.':
            tochka += 1
            if tochka < 2:
                new_chislo.append(i)
            else:
                break
        else:
            return None
    chislo = ''.join(new_chislo)
    if chislo != '':
        return float(chislo)
    else:
        return None


# модуль ввода
def calc(a):
    if a[1] == 1: # работа с рациональными числами
        strnum = 'рациональное число'   
        strnum1 = 'первое'
        strnum2 = 'второе'
    elif a[1] == 2: # работа с комплексными числами
        strnum = 'комплексное число'
        strnum1 = 'первое'
        strnum2 = 'второе'
    num1 = None

    while num1 is None:
        num1 = input(f'Введите {strnum1} {strnum} : ')
        num1 = check(num1)

    num2 = None
    while num2 is None:
        num2 = input(f'Введите {strnum2} {strnum} : ')
        num2 = check(num2)

    return (a[0], num1, num2)


# модуль меню
def menu():
    print("Дорогой пользователь! Приложение Калькулятор приветсвует тебя!")
    print("1. Рациональные числа")
    print("2. Комплексные числа\n")
    ok = False
    while not ok:
        p1 = input("Выберите, с какими числами будем работать?\nс рациональными - введите 1\nс комплексными - ввелите 2:\n")
        if p1.isdigit() and 1 <= int(p1) <= 2:
            ok = True
        else:
            print("Ошибка, введите 1 или 2")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    ok = False
    while not ok:
        p2 = input("Выберите арифметическое действие. Введите число от 1 до 4:")
        if p2.isdigit() and 1 <= int(p2) <= 4:
            ok = True
        else:
            print("Ошибка, введите число от 1 до 4")
    return (int(check(p2)), int(check(p1)))


# модуль калькуляции
def calcul(a):
    if a[0] == 1:
        result = str(a[1] + a[2])
    elif a[0] == 2:
        result = str(a[1] - a[2])
    elif a[0] == 3:
        result = str(a[1] * a[2])
    elif a[0] == 4 and a[2] != 0:
        result = str(a[1] / a[2]) #деление на 0
    else:
        result = 'Дейтсвие не поддерживается, вызывайте помощь'
    return(result)


vvod = menu() #p2-арифметическое действие, p1-тип чисел
vyrag = calc(vvod) #p2-арифметическое действие, 1 число, 2 число
print(calcul(vyrag))