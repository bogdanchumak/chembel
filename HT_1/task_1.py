# TASK 1
'''
1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
		Sample data : 1, 5, 7, 23
		Output :
		List : [‘1', ' 5', ' 7', ' 23']
		Tuple : (‘1', ' 5', ' 7', ' 23')
'''
values = input('Input comma-separated numbers: ')
list_example = values.split(',')
tuple_example = tuple(list_example)

print("Created list:", list_example)
print("Created tuple:", tuple_example)
