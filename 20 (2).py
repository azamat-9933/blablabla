"""
a = 6 
b = 7
c = 9
d = a * b * c

print(d)
"""
"""
a = int(input('a ni kiriting : '))

if a > 0 :
    print('true')
else :
    print('false')
"""
"""
# toq songa tekshirish
while True :
    a = int(input(' a ni kiriting : '))
    if a % 2 == 0 :
        print('true')
    else :
        print('false')
"""
"""
# juft songa tekshirish
while True :
    a = int(input(' a ni kiriting : '))
    if a % 2 == 1 :
        print('true')
    else :
        print('false')

"""
"""
a = int(input())
b = int(input())
c = int(input())

if a > 0 or b > 0:
    if b > 0 or c > 0:
        if a > 0 or c > 0:
            print('true')
        else :
            print('false')
    else :
        print('false')        
else :
    print('false')
"""
"""
# LIST 
b = 999
a = [1,2,2.5,3.2,"abc","acd",[1,2,3]]
# print(a[4])
print(a[6][2])
c = [3,4,5,6,7]
a.append(b) #a spisok oxiriga b ni qoship qo'yadi
a.extend(c) #a spisok + c spisok
a.insert(4,b) #a spisokni 4 ci elementini 1 ta o'ngga surib o'rniga b ni qo'yib qo'yadi
print(a.count(1))
print(a)
"""
# RANGE
"""
a = 1

if a in range(1,30,3):
    print(True)
"""
# FOR sikl
"""
c = [3.1,4,5,6,7]

for i in c:
    print(i)
"""
# project euler
"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""
# a = 0
# for x in range(10):
#     if x % 3 == 0 or x % 5 == 0 :
#         a = a + x
# print(a)

"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""

