# Name: Vipul Purohit
# Roll No: IC-2K24-96

n = 5
for i in range(1, n+1):
    print('*'*i + ' '*(2*(n-i)) + '*'*i)
for i in range(n, 0, -1):
    print('*'*i + ' '*(2*(n-i)) + '*'*i)
