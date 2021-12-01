'''
На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні,
   так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для
   кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
'''


class ValidationError(Exception):
    pass


def validation(username, password):
    number = 0
    for i in password:
        if i.isdigit():
            number += 1
    if 3 < len(username) < 50 and (len(password) > 8 and number > 0):
        print('Status: OK')
    elif len(username) <= 3:
        raise ValidationError
    elif len(password) < 8 or number == 0:
        raise ValidationError


list_of_users = {'user1': 'g123456789', 'slip': 'password'}


try:
    for username, password in list_of_users.items():
        print('Name:', username)
        print('Password:', password)
        validation(username, password)
except ValidationError:
    print(ValidationError('Status: Введіть валідні дані'))