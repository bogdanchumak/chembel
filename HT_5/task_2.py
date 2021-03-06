'''
Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :) (пароль повинен містити хоча б одну велику букву)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
'''


class ValidationError(Exception):
    pass


def validation(username, password):
    number = 0
    upper = 0
    for j in password:
        if j.isupper():
            upper += 1
    for i in password:
        if i.isdigit():
            number += 1
    if 3 < len(username) < 50 and (len(password) > 8 and number > 0 and upper > 0):
        print('Всі дані вірні')
    elif len(username) > 50 or len(username) <= 3:
        raise ValidationError("ім'я повинно бути не меншим за 3 символа і не більшим за 50")
    elif len(password) < 8:
        raise ValidationError('Пароль повинен бути не меншим за 8 символів')
    elif number == 0:
        raise ValidationError('Пароль повинен містити хоча б одну цифру')
    elif upper == 0:
        raise ValidationError('пароль повинен містити хоча б одну велику букву') # ЩОСЬ СВОЄ :)


validation('gs33', '1fhfghhfgh')
