import os

with open('5_1.txt', 'w') as file:
    while True:
        content = input('Write smth: ')
        file.write(content + '\n')
        if not content:
            break

# os.remove("f5_1.txt")


