'''
Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата,
і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
'''

def square(side):
    P = side * 4
    S = side * side
    d = side * (2 ** 0.5)
    result = (P, S, int(d))
    return result

print('Периметр, площа та діагональ квадрата:', square(2))