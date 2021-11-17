'''
Write a script to convert decimal to hexadecimal
		Sample decimal number: 30, 4
		Expected output: 1e, 04
'''

number = list(map(int, input().split()))
print('Decimal to hexdecimal:', end=' ')
for i in number:
    print(hex(i), end = ',')