'''
Write a script to check whether a specified value is contained in a group of values.
		Test Data :
		3 -> [1, 5, 8, 3] : True
		-1 -> (1, 5, 8, 3) : False
'''

list_of_numbers = list(map(int, input().split()))
number = int(input())
if number in list_of_numbers:
    print(True)
else:
    print(False)

