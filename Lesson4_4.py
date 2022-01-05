list_old = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_new = []
for i in range(len(list_old)):
    res = 0
    for j in range(len(list_old)):
        if list_old[i] == list_old[j]:
            res += list_old[j]
    if res == list_old[i]:
        list_new.append(list_old[i])
print(f"Исходный список: {list_old}")
print(f"Cписок без повторяющихся значений: {list_new}")

#Вариант, решенный на занятии
# from random import randint
#
# list_sour = [randint(0,10) for i in range(20)]
# print(f"Исходный список: {list_sour}")
#
# result = [el for el in list_sour if list_sour.count(el) == 1]
# print(f"В списке не повторяются числа: {result}")