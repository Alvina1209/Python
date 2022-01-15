class Worker:  # родительский класс
    def __init__(self, name, surname, position, wage, bonus):  # Спец метод
        self.name = name  # Атрибут экземпляра класс
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):  # Дочерний класс

    def get_full_name(self):  # Метод
        print(f'Имя сотрудника {self.name} {self.surname}')

    def get_total_income(self):  # Метод
        income = self._income.get('wage') + self._income.get('bonus')  # локальная переменная
        print(f'Доход сотрудника {income}')  # когда нужен return (если нет print)?

a = Position('Alex', 'Zotin','Manager', 200000, 50000)
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
a.get_full_name()
a.get_total_income()