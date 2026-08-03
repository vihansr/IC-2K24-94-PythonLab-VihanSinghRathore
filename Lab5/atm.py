# Name: Vipul Purohit
# Roll No: IC-2K24-96

balance = 5000
while True:
    print('\n1. Check Balance\n2. Withdraw\n3. Exit')
    opt = input('Choose: ')
    if opt == '1':
        print('Balance:', balance)
    elif opt == '2':
        w = int(input('Amount: '))
        if w <= balance:
            balance -= w
            print('Take your cash.')
        else:
            print('Insufficient funds')
    elif opt == '3':
        break
