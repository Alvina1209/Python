with open("5_2.txt", "r+", encoding="utf-8") as file:
    str1 = 0
    for line in file:
        str1 += 1 #счетчик
        words = line.split() #список из слов с разделителем " "
        num1 = len(words) #кол-во элементов в списке
        print(words)
        print(f"Строка {str1}, количество слов в ней = {num1}")






