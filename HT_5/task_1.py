'''
Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
   і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
       інакше (<silent> == <False>) - породжується виключення LoginException
'''


class LoginException(Exception):
    pass


def funct(username, password, silent = False):
    list_of_users = [{'user1': 123124, 'user2': 521, 'user3': 1525, 'user4': 435, 'user5': 1234}]
    for el in list_of_users:
        items = el.items()
    if (username, password) in items:
        print(True)
    elif (username, password) not in items and silent == True:
        raise LoginException


funct('user1', 123124, True)
