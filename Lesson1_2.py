# 2 Задание

# var1
sec = int(input("Введите время в секундах: "))
hour = sec // 3600
min = (sec - hour * 3600) // 60
sec = sec - hour * 3600 - min * 60
print(f'{hour:02}:{min:02}:{sec:02}')

# var2
sec = int(input("Введите время в секундах: "))
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
print(f'{hour:02}:{min:02}:{sec:02}')
