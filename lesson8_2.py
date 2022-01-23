
class MyError(Exception):  # дочерний класс от Exception

    def __init__(self, value):
        self.value = value

inp_data = input("Введите делитель: ")

try:
    inp_data = int(inp_data)
    if inp_data == 0:
        raise MyError("Вы ввели ноль, делить на него нельзя!")
except ValueError:
    print("Вы ввели не число")
except MyError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_data}")




