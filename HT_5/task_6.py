'''
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції -
   можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
'''
class Error(Exception):
    pass
def my_range(*args):
    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    else:
        raise TypeError()
    k = start
    result = []
    if step == 0:
        raise ValueError
    if k < stop and step < 0:
        raise Error('Введіть додатнє значення "step"')
    while k > stop and step > 0:
        result.append(k)
        k -= step
    while k < stop and step > 0:
        result.append(k)
        k += step
    while k > stop and step < 0:
        result.append(k)
        k += step
    yield result

print(*my_range(100, 55, -5))
