import json

with open("5_7.txt", "r+", encoding="utf-8") as file:
    with open("5_7.json", "w") as write_json:
        dict_res = {}
        dict_aver = {}
        title_1 = file.readline()
        count = 0
        profit_all = 0
        for line in file:
            line = line.rstrip()
            company, type_of_ownership, revenues, expenses = line.split()
            if (int(revenues) - int(expenses)) > 0:
                count += 1
                profit = int(revenues) - int(expenses)
                profit_all += profit
            else:
                loss = int(revenues) - int(expenses)
            dict_res[company] = profit if (int(revenues) - int(expenses)) > 0 else loss
        average_profit = int(profit_all/count)
        dict_aver["average_profit"] = average_profit
        list_all = [dict_res, dict_aver]
        print(list_all)
        print(type(list_all))

        json.dump(list_all, write_json)
        json_str = json.dumps(list_all)
        print(json_str)
        print(type(json_str))

