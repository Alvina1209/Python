def func_div(num_1, num_2):
    try:
        del_1 = num_1 / num_2
    except ZeroDivisionError:
        return
    return del_1

print(func_div(int(input("Введите делимое: ")), int(input("Введите делитель: "))))