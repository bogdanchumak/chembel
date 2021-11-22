'''
Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
   роботи захардкодити свій.
                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
'''

example_dict = {'a': 25, 'b': 22, 'c': 55, 'd': 55, 'f': [1, 2, 3]}
print('Initial dictionary: ', example_dict)

example_list = set(v for value in example_dict.values() for v in (
    value if isinstance(value, list) else [value]))


print('Dictionary without duplicates: ', set(example_list))




