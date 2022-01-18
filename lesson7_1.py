
class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for el in self.matrix:  # для каждого элемента списка (строки матрицы)
            for i in el:
                s = s + str(i) + '\t'
            s = s + '\n'
        return s
# или s = s + ' '.join(map(str, self.matrix[el])) + '\n' --> map можно использовать вместо for, принцип след.
# изначально принимается [0] элемент списка, т.е. [11,21,41], затем map начинает работать как итератор, для
# self.matrix[0] применяется str и после этого срабатывает ' '.join, т.е. объединение содержимого в строку через пробел,
# если str не будет, то выдаст ошибку, что это int, а не str, далее self.matrix[1] и т.д. до конца [11,21,41], затем
# проставляется '\n'. После этого все повторяется для следующих элементов списка.

# способ 1

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return print("Размерности не совпадают")
        s = ''
        for el_1, el_2 in zip(self.matrix, other.matrix):
            for i, j in zip(el_1, el_2):
                s = s + str(i+j) + '\t'
            s = s + '\n'
        return s

# способ 2

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return print("Размерности матриц не совпадают")
        res = self.matrix # задавая res таким образом, скрипт не падает, можно ли задать еще как-то, чтобы отработал?
# при res = '' появляется ошибка "string index out of range" в res[i][k]
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


l1 = [[7,8,9],[1,2,3],[-5,1,0]]
m = Matrix(l1)
print(m)
l2 = [[11,12,21],[22,33,44],[0,1,2]]
s = Matrix(l2)
print(s)
z = m + s
print(z)


