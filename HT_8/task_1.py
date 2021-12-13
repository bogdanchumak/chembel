"""
Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити"
   деяку кількість банкнот (вибирається номінал і кількість).
   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом -
   видається мінімальна кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного"
   алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) -
   в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн.,
   а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму
   (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).

   Особливості реалізації:
   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
     - переглянути наявні купюри;
     - змінити кількість купюр;
   - видача грошей для користувачів відбувається в межах наявних купюр;
   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й,
   наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.
"""


import csv
import json


def start():
    random = validation()
    if not random:
        return
    # Для адміна
    elif random == 'user4':
        while True:
            print("""
               Меню:
               1. Переглянути наявні купюри
               2. Завантажити купюри
               3. Вихід
            """)
            admin_option = input("Оберіть операцію:\n")
            if admin_option == '1':
                print('Наявні купюри:', view_collection())
            if admin_option == '2':
                print(collection())
            if admin_option == '3':
                return
            else:
                print('Операція не вірна! Спробуйте іншу')
    # Для простих смертних
    ans = True
    while ans:
        print("""Меню:
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


def collection():
    with open('bills.json', 'r+', encoding='utf-8') as file:
        file_reader = json.load(file)
        #for banknote_denomination, number_of_bills in file_reader.items():
            #print('Номінал купюри:', banknote_denomination, 'Кількість купюр даного номіналу:', number_of_bills)
        #print('\n')
        for banknote_denomination in file_reader.keys():
            if banknote_denomination == "10" and file_reader[banknote_denomination] >= 0:
                input_bills = int(input('Кількість десяток: '))
                if input_bills >= 0:
                    file_reader[banknote_denomination] += input_bills
                else:
                    input_bills = int(input('введіть ще раз: '))
                    file_reader[banknote_denomination] += input_bills
            if banknote_denomination == "20" and file_reader[banknote_denomination] >= 0:
                input_bills = int(input('Кількість двадцяток: '))
                if input_bills >= 0:
                    file_reader[banknote_denomination] += input_bills
                else:
                    input_bills = int(input('введіть ще раз: '))
                    file_reader[banknote_denomination] += input_bills
            if banknote_denomination == "50" and file_reader[banknote_denomination] >= 0:
                input_bills = int(input('Кількість пятдесяток: '))
                if input_bills >= 0:
                    file_reader[banknote_denomination] += input_bills
                else:
                    input_bills = int(input('введіть ще раз: '))
                    file_reader[banknote_denomination] += input_bills
            if banknote_denomination == "100" and file_reader[banknote_denomination] >= 0:
                input_bills = int(input('Кількість соток: '))
                if input_bills >= 0:
                    file_reader[banknote_denomination] += input_bills
                else:
                    input_bills = int(input('введіть ще раз: '))
                    file_reader[banknote_denomination] += input_bills
            if banknote_denomination == "200" and file_reader[banknote_denomination] >= 0:
                input_bills = int(input('Кількість двухсоток: '))
                file_reader[banknote_denomination] += input_bills
            if banknote_denomination == "500" and file_reader[banknote_denomination] >= 0:
                input_bills = int(input('Кількість пятисоток: '))
                if input_bills >= 0:
                    file_reader[banknote_denomination] += input_bills
                else:
                    input_bills = int(input('введіть ще раз: '))
                    file_reader[banknote_denomination] += input_bills
            if banknote_denomination == "1000" and file_reader[banknote_denomination] >= 0:
                input_bills = int(input('Кількість тисячних: '))
                if input_bills >= 0:
                    file_reader[banknote_denomination] += input_bills
                else:
                    input_bills = int(input('введіть ще раз: '))
                    file_reader[banknote_denomination] += input_bills
                file.close()


def view_collection():
    with open('bills.json', 'r+', encoding='utf-8') as file:
        file_reader = json.load(file)
        for banknote_denomination, number_of_bills in file_reader.items():
            print('Номінал купюри:', banknote_denomination, 'Кількість купюр даного номіналу:', number_of_bills)


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
    deposit_sum = int(input('Введіть суму поповнення: '))
    if deposit_sum < 0:
        f.write(current_deposit)
        print('Сума не вірна!')
        return
    else:
        summa = int(current_deposit) + deposit_sum
        f.write(str(summa))
        f.close()
        transactions('Користувачем ' + str(username) + ' поповнено рахунок на ' + str(deposit_sum) + ' рублів!',
                     username)
    return


def withdraw(username):
    current_deposit = view_balance(username)
    withdraw_input = int(input('Введіть суму: '))
    if withdraw_input > int(current_deposit):
        print('Недостатньо коштів на рахунку!')
        return withdraw(username)
    else:
        # Читання з файлу bills.json
        with open('bills.json', 'r', encoding='utf-8') as file:
            file_reader = json.load(file)
            for banknote_denomination, number_of_bills in file_reader.items():
                if banknote_denomination == '1000':
                    thousand = withdraw_input // 1000
                    number_of_bills -= thousand
                    file_reader['1000'] = number_of_bills
                    if thousand > 0:
                        print('Номінал купюрни:', banknote_denomination, 'Кількість:', thousand)
                elif banknote_denomination == '500':
                    five_hundred = ((withdraw_input % 1000) % 1000) // 500
                    number_of_bills -= five_hundred
                    file_reader['500'] = number_of_bills
                    if five_hundred > 0:
                        print('Номінал купюрни:', banknote_denomination, 'Кількість:', five_hundred)
                elif banknote_denomination == '200':
                    two_hundred = (((withdraw_input % 1000) % 1000) % 500) // 200
                    number_of_bills -= two_hundred
                    file_reader['200'] = number_of_bills
                    if two_hundred > 0:
                        print('Номінал купюрни:', banknote_denomination, 'Кількість:', two_hundred)
                elif banknote_denomination == '100':
                    one_hundred = ((((withdraw_input % 1000) % 1000) % 500) % 200) // 100
                    number_of_bills -= one_hundred
                    file_reader['100'] = number_of_bills
                    if one_hundred > 0:
                        print('Номінал купюрни:', banknote_denomination, 'Кількість:', one_hundred)
                elif banknote_denomination == '50':
                    fifty = (((((withdraw_input % 1000) % 1000) % 500) % 200) % 100) // 50
                    number_of_bills -= fifty
                    file_reader['50'] = number_of_bills
                    if fifty > 0:
                        print('Номінал купюрни:', banknote_denomination, 'Кількість:', fifty)
                elif banknote_denomination == '20':
                    twenty = ((((((withdraw_input % 1000) % 1000) % 500) % 200) % 100) % 50) // 20
                    number_of_bills -= twenty
                    file_reader['20'] = number_of_bills
                    if twenty > 0:
                        print('Номінал купюрни:', banknote_denomination, 'Кількість:', twenty)
                elif banknote_denomination == '10':
                    ten = (((((((withdraw_input % 1000) % 1000) % 500) % 200) % 100) % 50) % 20) // 10
                    number_of_bills -= ten
                    file_reader['10'] = number_of_bills
                    if ten > 0:
                        print('Номінал купюрни:', banknote_denomination, 'Кількість:', ten)
        # Запис в bills.json
        with open('bills.json', 'w', encoding='utf-8') as file:
            json.dump(file_reader, file, indent=1)
        # Запис в user_balance
        f = open(username + '_balance.csv', 'w', encoding='utf-8')
        summa = int(current_deposit) - withdraw_input
        f.write(str(summa))
        transactions('Користувачем ' + str(username) + ' знято ' + str(withdraw_input) + ' рублів!', username)
        f.close()
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
