# Вариант 1
def my_func(x, y):
    num_1 = x ** y
    return num_1

# Вариант 2
def my_func_2(x, y):
    num_1 = 1
    num_2 = 1
    for i in range(1, abs(y)+1):
        num_1 *= x
        if y > 0:
            num_2 = num_1
        else:
            num_2 = 1 / num_1
    return num_2

print(my_func(2,-8))
print(my_func_2(2,-8))