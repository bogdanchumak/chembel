'''
Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
   На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
   Кількість символів в блоках - та, яка введена в другому параметрі.
   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі
   (наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?)
   В репозиторій додайте і ті файли, по яким робили тести.
   Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл,
   а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість.
   В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
   Наприклад:
   █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
                     ⏫ центр

   █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно
                     ⏫ центр
'''

def my_func(file, number_of_symbols):
    with open(file, 'r', encoding='utf-8') as f:
        file_reader = f.read()
        middle = len(file_reader) // 2
        first = file_reader[0:number_of_symbols]
        last = file_reader[-number_of_symbols:]
        if len(file_reader) > 2:
            if number_of_symbols % 2 != 0:
                middle_of_string = file_reader[middle - number_of_symbols // 2:middle + number_of_symbols // 2 + 1]
            elif number_of_symbols % 2 == 0:
                middle_of_string = file_reader[middle - number_of_symbols // 2 + 1:middle + number_of_symbols // 2 + 1]
            new_list = [first, middle_of_string, last]
        elif len(file_reader) <= 2:
            new_list = [first, last]
    return new_list

print(my_func('example_symbols.txt', 3))
