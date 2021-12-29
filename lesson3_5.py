def sum_args():
    res = 0
    while True:
        list_1 = input("Введите числа через пробел: ").split(" ")
        for el in list_1:
            try:
                if el == "!":
                    return print(f"Сумма введенных значений {res}")
                else:
                    res += int(el)
            except ValueError:
                print("Введите число, чтобы продолжить, или ! для завершения")
        print(f"Сумма введенных значений {res}")


print(sum_args())

