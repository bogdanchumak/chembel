'''
Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j3453ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" ->
    просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
'''
'''
def my_func(random_string):
    if len(random_string) in range(30, 51):
        count = 0
        print('String length:', len(random_string))
        #for i in random_string:
            #if i.isdigit():
                #count += 1
        #print('Amount of digits:', count)
        count_of_letters = len(random_string) - count_of_digits
        print('Amount of letters: ', count_of_letters)
    elif len(random_string) < 30:
        print()
    return
'''
def my_func(random_string):
    if len(random_string) in range(30, 51):
        print('String length:', len(random_string))
        print('Count of digits:', count_of_digits(random_string))
        print('Count of letters:', count_of_letters(random_string))
    elif len(random_string) < 30:
        sum_of_numbers = 0
        string_without_digits = ''
        for i in random_string:
            if i.isdigit():
                sum_of_numbers += int(i)
        print('Sum of numbers:', sum_of_numbers)
        for letter in random_string:
            if not letter.isdigit():
                string_without_digits += letter
        print('String without digits:', string_without_digits)
    elif len(random_string) > 50:
        print("It's huge string!")
    return
def count_of_digits(random_string):
    count_of_digit = 0
    for i in random_string:
        if i.isdigit():
            count_of_digit += 1
    #print('Amount of digits:', count_of_digit)
    return count_of_digit
def count_of_letters(random_string):
    count_of_letter = len(random_string) - count_of_digits(random_string)
    #print(count_of_letter)
    return count_of_letter

random_string = str(input('Input string, please: '))

my_func(random_string)
