'''
Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
'''

def my_func(my_list):
    my_dict = {i: my_list.count(i) for i in my_list}
    return my_dict
my_list = [1, 1, 3, 3, 'a']

print(my_func(my_list))