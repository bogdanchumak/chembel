'''
Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
'''

def season(month):
    if month in range(1, 3):
        print('Winter')
    elif month in range(3, 6):
        print('Spring')
    elif month in range(6, 9):
        print('Summer')
    elif month in range(9, 11):
        print('Autumn')
    elif month == 12:
        print('Winter')
    return

month = int(input('Input number: '))

if month in range(1, 13):
    season(month)
else:
    print('Please input a number in range 1 to 12!')
    month = int(input('Input number: '))
