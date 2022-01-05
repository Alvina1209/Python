with open("5_5.txt", "w+") as file:
    file.write("22 77\n55 8 7")
    file.seek(0)
    sum_num = 0
    for line in file:# если будут не пробелы, будет ли итератор работать?
        num = line.split()
        for i in num:
            sum_num += int(i)
    print(sum_num)
    #print(file.tell())