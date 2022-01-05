with open("5_6.txt", "r+", encoding="utf-8") as file:
    dict_new = {} #создаю пустой словарь
    for line in file: #итерирую строки в текстовом файле (почему итератор реагирует на "\n" и только на него?)
        line = line.rstrip() #убираю \n
        content = line.split() #создаю список из слов, разделенных пробелом
        num_list = [] #создаю пустой список
        for word in range(len(content)): #итерирую каждый элемент списка
            num = ''  # создаю пустую строку
            for i in content[word]: #итерирую каждый символ элемента списка
                if ord(i) in range(48,58): #проверяю, является ли символ числом
                    num = num + i #если число, то складываю их в строку
                else:
                    if num != '': #если не число и ранее в "num" попали числа
                        num_list.append(int(num)) #добавляю это число как элемент списка
                        num = '' #очищаю, чтобы не было добавлено "num" при итерировании оставшихся символов в элементе
        sum_list = sum(num_list) #суммирую все элементы списка с числами в рамках одной строки
        dict_new[content[0].rstrip(":")] = sum_list #для каждой строки создаю в словаре ключ и соот-щее значение
    print(dict_new)


