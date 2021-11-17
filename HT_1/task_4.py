'''
Write a script to concatenate N strings.
'''

number_of_strings = int(input())
end_string = ''
for i in range(number_of_strings):
    random_string = input('Input string: ')
    end_string += random_string
print(end_string)
