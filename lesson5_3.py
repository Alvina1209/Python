# import sys
# print(sys.getdefaultencoding())
with open("5_3.txt", "r+", encoding="utf-8") as file:
    count = 0
    sum_sal = 0
    title = file.readline()
    for line in file:
        line = line.rstrip()
        surname, salary = line.split(", ")
        # count += 1 # для всех сотрудников
        # sum_sal += int(salary) # для всех сотрудников
        if int(salary) < 20000:
            print(surname, salary)
            count += 1 # для сотрудников с ЗП < 20
            sum_sal += int(salary) # для сотрудников с ЗП < 20
    print(f"Средняя величина дохода: {int(sum_sal / count)}")
