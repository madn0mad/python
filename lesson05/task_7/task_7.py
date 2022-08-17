"""
7)	Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить
ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

dlist = {}
res = []
cnt: int = 0
sum_pr_plus: int = 0
sum_pr_all: int = 0
with open('file7.txt', 'r', encoding='utf-8') as file7:
    flist = file7.readlines()
    for fline in flist:
        fname, ftype, fproceeds, fcosts = fline.split()
        if int(fproceeds) - int(fcosts) > 0:
            cnt += 1
            sum_pr_plus += int(fproceeds) - int(fcosts)
        sum_pr_all = int(fproceeds) - int(fcosts)
        dlist.update({fname: sum_pr_all})
    res.append(dlist)
    res.append({'average_profit': sum_pr_plus // cnt})

with open('file7.json', 'w', encoding='utf-8') as file7js:
    file7js.write(json.dumps(res,indent=4))
