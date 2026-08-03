# Name: Vipul Purohit
# Roll No: IC-2K24-96

n = int(input('How many terms? '))
n1 = 0
n2 = 1
print('Fibonacci series:')
for _ in range(n):
    print(n1, end=' ')
    n1, n2 = n2, n1 + n2
print()
