"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
try:
    with open('file2.txt', 'r', encoding='utf-8') as file2:
        f_lines = file2.readlines()
        print(f_lines)
        print(f'Количество строк в файле - {len(f_lines)}')
        i = 1
        for ln in f_lines:
            word_c = len(
                ln.replace('\n', '').replace(':', '').replace(',', '').replace('  ', ' ')
                .replace('.', '').split())
            print(f'Количество слов в {i}-й строке - {word_c}')
            i += 1
except IOError:
    print('Произошла ошибка ввода-вывода')
