class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        super().draw()
        print(f'Запуск отрисовки {self.title}')


class Penil(Stationery):

    def draw(self):
        super().draw()
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):

    def draw(self):
        super().draw()
        print(f'Запуск отрисовки {self.title}')


a = Stationery('Pen')
a.draw()

b = Pen('Pen')
b.draw()

c = Penil('Pencil')
c.draw()

d = Handle('Handle')
d.draw()