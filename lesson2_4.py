# 4 Задание

print("Введите ваш адрес, отделяя каждое слово пробелом: ")
my_list = input().split()
i = 0
for el in my_list:
    my_word = my_list[i]
    print(f'{i + 1}. {my_word[:10]}', end='\n')
    i += 1
