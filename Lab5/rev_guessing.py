# Name: Vihan Singh Rathore
# Roll No: IC-2K24-94

print('Think of a number between 1 and 10')
low = 1
high = 10
while low <= high:
    mid = (low + high) // 2
    ans = input(f'Is it {mid}? (y/h/l): ')
    if ans == 'y':
        print('Got it!')
        break
    elif ans == 'h':
        low = mid + 1
    else:
        high = mid - 1
