'''
Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
'''

def fibonacci(number):
    first_number, second_number = 1, 1
    for num in range(number):
        yield first_number
        if second_number < number:
            first_number, second_number = second_number, first_number + second_number
        else:
            break
fibonacci_list = list(fibonacci(15))
print('Числа Фібоначчі:', fibonacci_list)