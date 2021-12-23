# 5 Задание

sales = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))
if sales > cost:
    profit = (sales - cost) / sales
    num = int(input("Введите количество сотрудников фирмы: "))
    profit_1 = profit / num
    print(f'Фирма - прибыльная, прибыль фирмы в расчете на одного сотрудника = {profit_1:.0}')
else:
    print('Фирма - убыточная')
