with open("5_4.txt","r", encoding="utf-8") as file:
    for line in file:
        line = line.rstrip()
        words, number = line.split(" — ")
        my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        if words in my_dict.keys():
            words = my_dict.get(words)
        print(f"{words} - {number}")