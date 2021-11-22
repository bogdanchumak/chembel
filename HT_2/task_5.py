'''
Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
   роботи захардкодити свій.
                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
'''

example_dict = {'a': 25, 'b': 22, 'c': 55, 'd': 55, 'f': [1, 2, 3]}
new_dict = {}
for key, value in example_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value

print('Output:', new_dict)




