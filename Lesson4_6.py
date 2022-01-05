import sys
from itertools import count, cycle


for el in count(3):
    if el > 10:
        break
    else:
        print(el)

list = ['Лиля','Юрьевна','Брик']
k = 0
for el in cycle(list):
    if k > 10:
        break
    else:
        print(el)
    k += 1

#Вариант с занятия
# start_from = 10
# iterable = 'ABCDEF'
# iteration_count = 0
#
# def integer_generator(start_from):
#     for el in count(start_from):
#         if el > start_from+100:
#             break
#         yield el
#
# for el in integer_generator(15):
#     print(el)
#
# gen = integer_generator(10)
# print(gen)
# print(sys.getsizeof(gen)) #какой объем занимает в памяти
# print(sys.getsizeof(list(gen)))

