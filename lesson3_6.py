def int_func():
    words = input("Введите слова из латинских букв, отделенных пробелом: ").split()
    res = []
    for el in words:
        res.append(el.capitalize())
    return " ".join(res)

print(int_func())
