# from functools import reduce
# from itertools import count
# from math import factorial

def fact(n):
    if n == 0:
        yield 1
    elif n < 0:
        print("Введите неотрицательное число")
    else:
        res = 1
        for el in range(1, n + 1):
            res *= el
            yield res

for el in fact(5):
    print(el)

#Решение с занятия
# def fact(n):
#     # result = 1
#     for i in count(1):
#         if i <= n:
#             # result *= i
#             # result = factorial(i)
#             result = reduce(lambda x, y: x*y, range(1,i+1))
#             yield result
#         else:
#             break
#
# for el in fact(5):
#     print(el)