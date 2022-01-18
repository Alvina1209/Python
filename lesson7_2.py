from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod # абстрактный метод --> функция expense д.б. в дочерних классах, иначе скрипт не отработает
    def expense(self):
        pass


class Coat(Clothes):

    @property # декоратор --> для удобства, чтобы при вызове expense не нужно было бы указывать expense()
    def expense(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def expense(self):
        return self.param * 2 + 0.3


a = Coat(52)
b = Suit(1.80)
print(a)
print(a.expense)
print(b.expense)
