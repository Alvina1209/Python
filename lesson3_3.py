def my_func(num_1, num_2, num_3):
    min_num = -min(num_1, num_2, num_3)
    answer_1 = sum([num_1, num_2, num_3, min_num])
    return answer_1

print(my_func(3,2,5))