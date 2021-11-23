'''
Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi,
обробляє повернутий ними результат та також повертає результат.

Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
'''


def custom_sum(x, y):
    return x + y


def custom_diff(x, y):
    return x - y


def custom_product(x, y):
    return x * y


def func_4():
    f1 = custom_sum(12, 4)
    f2 = custom_diff(10, 4)
    f3 = custom_product(1, 2)
    return f1 + f2 + f3



print('Output:', func_4())