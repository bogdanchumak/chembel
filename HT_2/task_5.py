'''
Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
   роботи захардкодити свій.
                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
'''

example_dict = {'a': 25, 'b': 22, 'c': 55, 'd': 55}
print('Initial dictionary: ', example_dict)
print('Dictionary without duplicates: ',
      {v:k for k,v in {example_dict[k]:k for k in reversed(list(example_dict))}.items()})




