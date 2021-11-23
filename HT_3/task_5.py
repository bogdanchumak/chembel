'''
Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї),
    пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y"
    і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z
'''

def my_custom_function(x, y):
    if x > y:
        z = x - y
        return print('х бiльше нiж у на', z)
    elif x < y:
        z = y - x
        return print('y більше ніж х на', z)
    elif x == y:
        return print('х дорiвнює z')

x = int(input('Input x: '))
y = int(input('Input y: '))

my_custom_function(x, y)