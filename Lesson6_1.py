from itertools import cycle
from time import sleep

class TrafficLight:
    __dict_color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def __init__(self, color):  #  какая разница в __color и color (работает в 2-х вариантах)?
        self.__color = color

    def running(self):
        my_dict = cycle(self.__dict_color.items())
        for color_new, time_new in my_dict:
            if self.__color == color_new:
                print(f'Сейчас горит: {color_new}')
                print(f'Через {time_new} сек. цвет изменится')
                sleep(time_new)
                color = next(my_dict)
                self.__color = color[0]

a = TrafficLight('Желтый')
a.running()

# код с занятия

# class TrafficLight:
#     colors_queue = ('красный', 'желтый', 'зеленый')
#     time_queue = (7, 2, 5)
#     message = ('красный - проезда нет', 'желтый - будь готов', 'зеленый - езжай')
#
#     def __init__(self, color):
#         self.__color = color
#
#     def running(self):
#         my_cycle = cycle(self.colors_queue)
#         for traffic_color in my_cycle:
#             if self.__color == traffic_color:
#                 print(self.message[self.colors_queue.index(self.__color)])
#                 sleep(self.time_queue[self.colors_queue.index(self.__color)])
#                 self.__color = next(my_cycle)
#
#
# my_traffic = TrafficLight('зеленый')
# my_traffic.running()




