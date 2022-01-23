
class MyError(Exception):

    def __init__(self, value):
        self.value = value

inp_list = [1,54,0,[1]]

try:
    for elem in inp_list:
        if not isinstance(elem, int):
            raise MyError("В списке содержатся не только числа")
except MyError as err:
    print(err)
else:
    print("В списке содержатся только числа")



