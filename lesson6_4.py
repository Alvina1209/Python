class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} тронулась')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} направляется {self.direction }')

    def show_speed(self):
        print(f'Средняя скорость {self.name} составляет {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Осторожно, вы превысили скорость, это городской автомобиль.' \
                  f' Он является полицейской машиной? {self.is_police}')
        else:
            print(f'Скорость {self.speed}. Он является полицейской машиной? {self.is_police}')

class SportCar(Car):

    def show_speed(self):
        print(f'Скорость {self.speed}. Он является полицейской машиной? {self.is_police}')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Осторожно, вы превысили скорость, это автомобиль для работы.' \
                  f' Он является полицейской машиной? {self.is_police}')
        else:
            print(f'Скорость {self.speed}. Он является полицейской машиной? {self.is_police}')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police = True)

    def show_speed(self):
        print(f'Скорость {self.speed}. Он является полицейской машиной? {self.is_police}')

a = Car(60, 'Синий', 'Volvo')
a.go()
a.stop()
a.turn('на дачу')
a.show_speed()

b = TownCar(70, 'Красный', 'AUDI')
b.go()
b.stop()
b.turn('в парк')
b.show_speed()

c = SportCar(70, 'Красный', 'Ferrari')
c.go()
c.stop()
c.turn('на трассу')
c.show_speed()

d = WorkCar(70, 'Черный', 'Mercedes')
d.go()
d.stop()
d.turn('в офис')
d.show_speed()

e = PoliceCar(70, 'Белая', 'Lada')
e.go()
e.stop()
e.turn('к клиенту')
e.show_speed()
