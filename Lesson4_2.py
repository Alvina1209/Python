# мой вариант
list_old = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_new = [list_old[i] for i in range(1, len(list_old))]
list = [list_new[i] for i in range(len(list_new)) if list_new[i] > list_old[i]]

print(f"Исходный список: {list_old}")
print(f"Новый список: {list}")

# с разбора дз
list_old = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list = [list_old[i] for i in range(1, len(list_old)) if list_old[i] > list_old[i-1]]

print(f"Исходный список: {list_old}")
print(f"Новый список: {list}")
