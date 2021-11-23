'''
Створити цикл від 0 до ... (вводиться користувачем).
В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.
'''

user_number = int(input('Input number: '))

for num in range(0, user_number + 1):
    if num % 17 == 0:
        print('Numbers divisible by 17: ', num)