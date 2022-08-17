"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

try:
    with open('file3.txt', 'r', encoding='utf-8') as file3:
        flines = file3.readlines()
        print('Сотрудники с окладом менее 20.000р.: \n')
        sum_inc: int = 0
        for fls in flines:
            if int(fls.split()[1].split('.')[0]) > 20000:
                sum_inc += int(fls.split()[1].split('.')[0])
                print(fls.split(' ')[0])
        print(f'\nСредняя величина дохода сотрудников - {sum_inc / len(flines)}')

except IOError:
    print('Произошла ошибка ввода-вывода!')
