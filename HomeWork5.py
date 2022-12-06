# 1. Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14
#     Ввод: 0.001
#     Вывод: 3.141

import math
y = input('Введите с какой точностью показать число π - ')
z = y.split('.')
l = len(z[1])
p = round(math.pi, l)
print(p)

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input('Введите число от 2 вкючительно- '))
count = 0
r = 0
for x in range(2,n):
    if x != n:
        r = n%x
        if r == 0:
            count +=1
if count > 0:
    print('число составное')
else: print('число простое')
        
3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
Ввод: [1, 1, 2, 3, 4, 4, 4]
Вывод: [2, 3]
list = input('Введите через пробел последовательность чисел - ').split(' ')
list2 = []
e = len(list)
for x in range(e):
    count = 0
    f = x +1
    for y in range(e):
        if x != y:
            if list[x] == list[y]:
                count = count + 1
    if count == 0:
        list2.append(list[x])
print('Ввод:',list)
print('Вывод:',list2)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random
k = int(input('Введите значение натуральной степени к - '))
index = 0
r = 0
s = str()
j = str()
for x in range(k):
    k = k - index
    index = 1
    j = str(k)
    r = str(random.randint(0, 100))
    s = s + r + '*' + '(x**' + j + ')' + '+'
r = str(random.randint(0, 100))
s = s + r + ' = 0'
print(s)


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).


q = input('Введите первый многочлен - ')
with open('f1.txt', 'w') as f_data:
    f_data.write(q)
q1 = input('Введите второй многочлен - ')
with open('f2.txt', 'w') as f_data:
    f_data.write(q1)
s = q.split('+')
s1 = q1.split('+')
t = len(s)
print(s)
print(s1)
for x in range(len(s1)):
    s.append(s1[x])
print(s)
x = 0
x1 = t
print(x1)
y1 = x1
plus = x1
formula = str()
count = 0
while len(s) >= 1:
    box = s[0].split('^')
    step = box[1]
    box = box[0]
    liter = box[-1]
    if len(box) == 1:
            index = 1
    elif len(box) > 1:
            index = box[:-1]
    index = box[:-1]
    y = 1
    count = 0
   
    while len(s) >= 2:
        box1 = s[y].split('^')
        step1 = box1[1]
        box1 = box1[0]
        liter1 = box1[-1]
        if len(box1) == 1:
            index1 = 1
        elif len(box1) > 1:
            index1 = box1[:-1]
        count = 0
        
        if liter == liter1 and step == step1:
            sum = int(index) + int(index1)
            formula = str(formula) + str(sum) + str(liter) + '^' + str(step)
            if sum != 0 and x < plus:
                formula = str(formula) + '+'
            s.pop(y)
            count += 1
            break
        y += 1
        if y == len(s):
            break
    
    if count == 0:
        formula = str(formula) + str(index) + str(liter) + '^' + str(step)
        if sum != 0 and y < plus:
                formula = str(formula) + '+'
    s.pop(0)
    
print(formula)



