# if a == b:
#     print(a)


# a = int(input("a ni kiriting : "))
# b = int(input("b ni kiriting : "))
# while a != b:
#     b = b - 1
#     print(b)
# else:
#     print('cant find')

b = 0
while True:
    a = int(input())
    if a != 0:
        b = a + b
    else:
        print("summa :", b)