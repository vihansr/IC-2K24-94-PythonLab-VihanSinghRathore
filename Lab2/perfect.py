# Name: Vipul Purohit
# Roll No: IC-2K24-96

num = int(input('Enter a number: '))
divisors_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisors_sum += i
if divisors_sum == num:
    print('Perfect number')
else:
    print('Not a perfect number')
