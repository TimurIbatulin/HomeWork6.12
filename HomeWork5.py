# 1. Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14
#     Ввод: 0.001
#     Вывод: 3.141

# import math
# y = input('Введите с какой точностью показать число π - ')
# z = y.split('.')
# l = len(z[1])
# p = round(math.pi, l)
# print(p)

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# n = int(input('Введите число от 2 вкючительно- '))
# count = 0
# r = 0
# for x in range(2,n):
#     if x != n:
#         r = n%x
#         if r == 0:
#             count +=1
# if count > 0:
#     print('число составное')
# else: print('число простое')
        
# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]
# list = input('Введите через пробел последовательность чисел - ').split(' ')
# list2 = []
# e = len(list)
# for x in range(e):
#     count = 0
#     f = x +1
#     for y in range(e):
#         if x != y:
#             if list[x] == list[y]:
#                 count = count + 1
#     if count == 0:
#         list2.append(list[x])
# print('Ввод:',list)
# print('Вывод:',list2)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

# import random
# k = int(input('Введите значение натуральной степени к - '))
# index = 0
# r = 0
# s = str()
# j = str()
# for x in range(k):
#     k = k - index
#     index = 1
#     j = str(k)
#     r = str(random.randint(0, 100))
#     s = s + r + '*' + '(x**' + j + ')' + '+'
# r = str(random.randint(0, 100))
# s = s + r + ' = 0'
# print(s)

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

q = input('Введите первый многочлен - ')
with open('f1.txt', 'w') as f_data:
    f_data.write(q)
q1 = input('Введите второй многочлен - ')
with open('f2.txt', 'w') as f_data:
    f_data.write(q1)
s = q.split('+')
print(s)
ql = list(q)
ql2 = list(q1)
print(ql)
l1 = len(ql)
print(l1)
l2 = len(ql2)
d = str()
p = str()
qll = []
x = 0
while x < l1:
    z = ql[x]
    print(f'z = ', z)
    while z.isdigit():
        p = str(z)
        d = str(d) + p
        print(f'd = ', d)
        x += 1
        z = ql[x]
        print(f'z2 = ', z)
    qll.append(d)
    d = str()
    if z == '(':
        tt = x + 6
        while x < tt:
            e = ql[x]
            d = d + str(e)
            x += 1
        qll.append(d)
        d = str()
    if z == '*' or z == '+' or z == '-':
        x += 1


print(qll)






# l1 = len(ql)          44*(x**2)+356*(x**3)
# l2 = len(ql2)
# for x in range(l1):
#     for y in range(l2):
#         if ql[x] == ql2[y]:
#             x1 = x - 1
#             y1 = y - 1
#             x4 = x + 4
#             y4 = y + 4
#             x3 = x + 3
#             y3 = y + 3
#             if ql[x1] == ql2[y1] and ql[x4] == ql2[y4] and ql[x3] == ql[y3]:
#                 if x > 3:
#                     xd = x - 3
#                     for p in range(xd, 0, -1):
#                         if xd > 0:
#                             xd1 = xd - 1
#                             if ql[xd1] == ql[xd1].isdigit():
#                                 mn = 


    

# print(ql)

