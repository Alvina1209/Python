# 4 Задание

n = input("Введите целое положительное число: ")
i = 1
k = 10
num = len(n)
n = int(n)
numbers_list = []
while num > 0:
    z = n // (k ** (num-1))
    numbers_list.append(z)
    n = n - z * (k ** (num - 1))
    max_number = max(numbers_list)
    num -= 1
    i += 1
print(max_number)
