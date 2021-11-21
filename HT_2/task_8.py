'''
Написати скрипт, який отримує від користувача позитивне ціле число і створює словник, з ключами від 0 до введеного числа,
   а значення для цих ключів - це квадрат ключа.
        Приклад виводу при введеному значенні 5 :
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
user_number = int(input('Input number: '))
example_dictionary = {a: a ** 2 for a in range(0, user_number + 1)}
print('New dictionary:', example_dictionary)