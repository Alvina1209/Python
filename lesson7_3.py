
class Cell():

    def __init__(self, param):
        self.param = param

    def __str__(self):
        return str(f'Количество ячеек - {self.param}')

    def __add__(self, other):
        return Cell(self.param + other.param)

    def __sub__(self, other):
        return Cell(max(self.param, other.param) - min(self.param, other.param))

    def __mul__(self, other):
        return Cell(self.param * other.param)

    def __truediv__(self, other):
        return Cell(self.param // other.param)

    def make_order(self, count):
        x = self.param
        while x > 0:
            for el in range(1, count + 1):
                print('*', end='')
                x -= 1
                if x <= 0:
                    break
            print('\\n', end='') if x > 0 else ''


a = Cell(11)
b = Cell(5)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

a.make_order(3)
print('\n----------')
b.make_order(3)