'''
Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи
- один з яких операцiя, яку зробити!
'''

def calculate(x, y, z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '*':
        return x * y
    elif z == '/':
        return x / y
    elif z == '//':
        return x // y
    return
x, z, y = input('Input something: ').split()
result = calculate(int(x), int(y), z)
print('Output:', result)