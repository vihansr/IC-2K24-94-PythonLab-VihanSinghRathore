# Name: Vihan Singh Rathore
# Roll No: IC-2K24-94

num = int(input('Enter a number: '))
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10
if num == total:
    print(num, 'is an Armstrong number')
else:
    print(num, 'is not an Armstrong number')
