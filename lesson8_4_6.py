class Storage:

    def __init__(self, name, price, amount, number_of_lists, *args):
        self.name = name
        self.price = price
        self.amount = amount
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.amount}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.amount}'

    def reception(self):
        try:
            unit = input('Введите наименование ')
            unit_p = int(input('Введите цену за ед '))
            unit_a = int(input('Введите количество '))
            my_dict = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_a}
            self.my_unit.update(my_dict)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return 'Ошибка ввода данных'

        # print('Для выхода - Q, продолжение - Enter')
        q = input('Для выхода - Q, продолжение - Enter: ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return 'Выход'
        else:
            return Storage.reception(self)


class Printer(Storage):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Storage):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Storage):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


a = Printer('hp', 2000, 5, 10)
b = Scanner('Canon', 1200, 5, 10)
c = Copier('Xerox', 1500, 1, 15)
print(a.reception())
print(a.to_print())
print(c.to_copier())


