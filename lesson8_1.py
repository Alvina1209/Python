import re

class Date():

    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def format_date(cls, day_month_year):
      num = re.findall(r'\d+', day_month_year)
      return int(num[0]), int(num[1]), int(num[2])

    @staticmethod
    def valid_format(day_month_year):
        my_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        num = re.findall(r'\d+', day_month_year)
        if len(num[2]) < 5 and my_dict.get(int(num[1])) >= int(num[0]):
            print("Данные введены корректно:")
        else:
            print("Введите корректные даты:")
        return Date.format_date(day_month_year)

print(Date.valid_format('12-12-2022'))
print(Date.valid_format('31-01-2021'))
print(Date.valid_format('32-12-2021'))



