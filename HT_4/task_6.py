'''
Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне,
збільшити його на 100, якщо дорівнює 0, не змінювати.
'''

def my_func(number):
    if number > 0:
        print('Квадрат додатнього числа:', number*number)
    elif number < 0:
        number = number + 100
        print(number)
    elif number == 0:
        None
    return
n = my_func(number=int(input()))


