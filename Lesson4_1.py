from sys import argv

script_name, volume, rate, premium = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", volume)
print("Ставка в час: ", rate)
print("Премия: ", premium)
print("ЗП: ", (int(volume) * int(rate)) + int(premium))

# Отработка через терминал: python lesson4_1.py 50 3 100
