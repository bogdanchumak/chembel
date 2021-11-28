'''
Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте, и False - якщо ні.
'''

def is_prime(number):
    if number > 1:
        for i in range (2, number - 1):
            if (number % i) != 0:
                continue
            else:
                return False
    return True

print(is_prime(18))