vhod = ' 12.434.4'

new_chislo = []
vhod = vhod.replace(',','.').replace(' ','') #заменяем на точки и убиарем пробелы
koef = ''
tochka = 0
for i in vhod:
    if i == '-':
        koef = '-'
    if i.isdigit():
        new_chislo.append(koef + i)
        if koef == '-':
            koef = ''
    if i == '.':
        tochka += 1
        if tochka < 2:
            new_chislo.append(i)
        else:
            break
chislo = ''.join(new_chislo)
if chislo != '':
    print(float(chislo))
else:
    print(None)