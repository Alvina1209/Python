
class Road:
     def __init__(self, length, width): # конструктор, self - определяет ссылку на объект (экземпляр) класса
       self._length = length
       self._width = width

     def weights(self, weight, depth):
       res = int(self._length * self._width * weight * depth / 1000)
       return  print(f' Масса асфальта, необходимого для покрытия всего дорожного полотна, составляет {res} т')

a = Road(20, 5000)
a.weights(25, 5)

# вариант, решенный на занятии

# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def square(self):
#         return self._length * self._width
#
#     def get_weight_of_asphalt(self, weight_ratio, thikness):
#         asphalt = self.square() * weight_ratio * thikness
#         return asphalt
#
# my_road = Road(20,5000)
# print(my_road.get_weight_of_asphalt(25, 5))


