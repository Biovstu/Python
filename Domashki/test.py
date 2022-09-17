# a_r = 2.5
# a_i = 2
#
# a = complex(a_r, a_i)
# b = complex(1, 3)
# print('a - b =', a - b)
#
# def print_complex(a: complex):
#     if a.imag == 0:
#         return int(a.real) if a.real.is_integer() else a.real
#     else:
#         return a
#
# print('a - b =', print_complex(a - b))

a = float('-inf')
print(a)
b = float('+inf')
print(b)

c = (a, b)
print(c)
print((c[0] + c[1]) / 2)