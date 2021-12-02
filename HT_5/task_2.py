'''
Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
'''


class ValidationError(Exception):
    pass


def validation(username, password):
    number = 0
    for i in password:
        if i.isdigit():
            number += 1
    if 3 < len(username) < 50 and (len(password) > 8 and number > 0):
        print('Всі дані вірні')
    elif len(username) > 50:
        print('Введіть нормальний логін')
    else:
        raise ValidationError('Something went wrong')

validation('gsdgsd', '1gfhfghfgh')