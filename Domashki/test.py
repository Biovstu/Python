tmp = ['12.4', '0']

def check(vhod):
    new_chislo = []
    vhod = vhod.replace(',', '.').replace(' ', '')  # заменяем на точки и убиарем пробелы
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


print(check(tmp[0]) is not None)
print(check(tmp[1]) is not None)
print(check(tmp[0]) is not None and check(tmp[1]) is not None)