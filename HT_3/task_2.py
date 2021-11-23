'''
Користувачем вводиться початковий і кінцевий рік.
Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).
'''

initial_year = int(input('Input initial year: '))
last_year = int(input('Input last year: '))

for years in range(initial_year, last_year + 1):
    if years % 400 == 0 or (years % 4 == 0 and years % 100 != 0):
        print('A leap year:', years)