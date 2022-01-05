from functools import reduce
def my_func(el1, el2):
    return el1 * el2

print([i for i in range(100,1001) if i % 2 == 0])
print(reduce(my_func, [i for i in range(100,1001) if i % 2 == 0]))

#Вариант, решенный на занятии
# list_sour = [el for el in range(100,1001,2)]
# print(list_sour)
#
# res = reduce(lambda x, y: x*y, list_sour)
# print(res)