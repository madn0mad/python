"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randrange

with open('file5.txt', 'w+', encoding='utf-8') as file5:
    l = [randrange(1, 300, 10) for i in range(10)]
    n_sum: int = 0
    for item in l:
        file5.write(f' {item}')
        n_sum += int(item)
print(f'Сумма цифр в файле равна {n_sum}')
