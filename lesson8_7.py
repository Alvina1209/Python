class Complex():

    def __init__(self, integer):
        self.integer = integer

    def __add__(self, other):
        integer_1 = self.integer
        integer_2 = other.integer
        my_list_1 = integer_1.strip().split('+')
        my_list_2 = integer_2.strip().split('+')
        complex_1 = 0
        complex_2 = 0
        int_1 = 0
        int_2 = 0
        for elem_1 in my_list_1:
            if elem_1.strip().find("i") > 0:
                complex_1 = int(elem_1.strip().rstrip("i"))
            else:
                int_1 = int(elem_1)
        for elem_2 in my_list_2:
            if elem_2.strip().find("i") > 0:
                complex_2 = int(elem_2.strip().rstrip("i"))
            else:
                int_2 = int(elem_2)
        complex_sum = complex_1 + complex_2
        int_sum = int_1 + int_2
        if int_sum > 0:
            sign = '+'
        else:
            sign = '-'
        print(f"{complex_sum}i {sign} {abs(int_sum)}")

    def __mul__(self, other):
        integer_1 = self.integer
        integer_2 = other.integer
        my_list_1 = integer_1.strip().split('+')
        my_list_2 = integer_2.strip().split('+')
        complex_1 = 0
        complex_2 = 0
        int_1 = 0
        int_2 = 0
        for elem_1 in my_list_1:
            if elem_1.strip().find("i") > 0:
                complex_1 = int(elem_1.strip().rstrip("i"))
            else:
                int_1 = int(elem_1)
        for elem_2 in my_list_2:
            if elem_2.strip().find("i") > 0:
                complex_2 = int(elem_2.strip().rstrip("i"))
            else:
                int_2 = int(elem_2)
        int_sum = int_1*int_2-complex_1*complex_2
        complex_sum = int_1*complex_2+int_2*complex_1
        if int_sum > 0:
            sign = '+'
        else:
            sign = '-'
        print(f"{complex_sum}i {sign} {abs(int_sum)}")


a = Complex('4i + 7')
b = Complex('7i')
c = a + b
print(c)
d = a*b
print(d)

