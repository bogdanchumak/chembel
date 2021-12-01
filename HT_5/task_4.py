'''
Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100),
кожен елемент якого буде ділитись без остачі на 5 але не буде ділитись на 3.
   Перевірка: [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95]
'''

example_list = [el for el in range(0, 100) if el % 5 == 0 or not el/3]
print('List', example_list)