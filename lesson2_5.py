# 5 Задание

my_list = [1, 7, 5, 3, 3, 2]
el = input("Введите новое число:\n")
print(el)
while True:
    try:
        if el == '!':
            break
        else:
            el = int(el)
            my_list.append(el)
            my_list.sort(reverse=True)
            print(my_list)
            el = input("Введите новое число:\n")
    except ValueError:
        print("Вы ввели не числовое значение, повторите попытку, для прекращения введите !")
        el = input("Введите новое число:\n")
