'''
Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
і вертатиме список простих чисел всередині цього діапазона.
'''

def prime_list(begin_of_range, end_of_range):
    prime_list = list()
    for number in range(begin_of_range, end_of_range):
        count = 0
        divisor = 2
        while divisor < number:
            if number % divisor == 0:
                count += 1
            divisor += 1
        if count == 0:
            prime_list.append(number)
    return prime_list

print('Список простих чисел:', prime_list(16, 45))