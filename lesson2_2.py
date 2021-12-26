# 2 Задание

print("Введите свое имя, отделяя каждую букву пробелом: ")
my_list = input().split()
len_list = len(my_list)
if len_list % 2 == 0:
    my_list[1::2], my_list[::2] = my_list[::2], my_list[1::2]
else:
    my_list[1:len_list - 1:2], my_list[:len_list - 1:2] = my_list[:len_list - 1:2], my_list[1:len_list - 1:2]
print(my_list)



