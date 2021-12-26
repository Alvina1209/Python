# 3 Задание

my_month = int(input("Введите номер месяца:\n "))
my_list = ['Весна', 'Лето', 'Осень', 'Зима']
# Вариант 1
if 3 <= my_month <= 5:
    print(my_list[0])
elif 6 <= my_month <= 8:
    print(my_list[1])
elif 9 <= my_month <= 11:
    print(my_list[2])
else:
    print(my_list[3])
# Вариант 2
my_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', \
           10: 'Осень', 11: 'Осень', 12: 'Зима'}
print(my_dict[my_month])