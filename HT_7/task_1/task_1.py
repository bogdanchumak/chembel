'''
Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій
      (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних
      (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача -
        не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні -
        вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)
'''
import csv
import json


def start():
    random = validation()
    if not random:
        return
    ans = True
    while ans:
        print("""
                MENU:
                1: Поточний баланс
                2: Поповнити баланс
                3: Зняти кошти
                4: Вихід
                """)
        option = input("Оберіть операцію:\n")
        if option == '1':
            print('Поточний баланс:', view_balance(random))
        if option == '2':
            make_a_deposit(random)
        if option == '3':
            withdraw(random)
        if option == '4':
            print('Гарного дня!')
            return


def transactions(value, username):
    with open(username + '_transactions.json', 'a', encoding='utf-8') as file:
        json.dump({value: 'Transaction'}, file, indent=1, ensure_ascii=False)
    return


def view_balance(username):
    f = open(username + '_balance.csv', 'r')
    balance = f.read()
    return balance


def make_a_deposit(username):
    current_deposit = view_balance(username)
    f = open(username + '_balance.csv', 'w', encoding='utf-8')
    deposit_summ = int(input('Введіть суму поповнення: '))
    if deposit_summ > 0:
        summ = int(current_deposit) + deposit_summ
        f.write(str(summ))
        f.close()
        transactions('Користувачем ' + str(username) + ' поповнено рахунок на ' + str(deposit_summ) + ' рублів!', username)
    else:
        print('Сума не вірна!')
        return
    return


def withdraw(username):
    current_deposit = view_balance(username)
    f = open(username + '_balance.csv', 'w', encoding='utf-8')
    withdraw_summ = int(input('Введіть суму: '))
    if withdraw_summ > 0:
        summ = int(current_deposit) - withdraw_summ
        if summ < 0:
            f.write(current_deposit)
            print('Недостатньо коштів!')
        else:
            f.write(str(summ))
            transactions('Користувачем ' + str(username) + ' знято ' + str(withdraw_summ) + ' рублів!', username)
    else:
        print('Сума не вірна!')
        return
    return


def validation():
    user_info = get_info()
    user_input_login = input('Input login: ')
    for n in user_info:
        if user_input_login == n[0]:
            user_input_password = str(input('Input password: '))
            if user_input_password == n[1]:
                print('Logged in!')
                return user_input_login
            else:
                print('Password incorrect!')
                return None
    print('User not found!')
    return None


def get_info():
    with open('users.csv', 'r', newline='') as f:
        a = []
        file_reader = csv.reader(f, delimiter=',')
        for row in file_reader:
            a.append(row)
    return a


start()
