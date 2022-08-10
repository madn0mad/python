"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

n = int(input('Введите номер месяца: '))
months_l = ('Зима', 'Весна', 'Лето', 'Осень')
if 0 < n <= 3 or n == 12:
    print(f'Результат через список: {months_l[0]}')
elif 3 <= n <= 5:
    print(f'Результат через список: {months_l[1]}')
elif 6 <= n <= 8:
    print(f'Результат через список: {months_l[2]}')
elif 9 <= n < 12:
    print(f'Результат через список: {months_l[3]}')
else:
    print("Введено недопустимое число")

months_d = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
            9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима', }
print(f'Результат через словарь: {months_d[n]}')
