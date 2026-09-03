# Name: Vipul Purohit
# Roll No: IC-2K24-96

contacts = {'Vipul': '9876543210', 'Rahul': '9123456780'}
name = input('Enter name to search: ')
if name in contacts:
    print('Number:', contacts[name])
else:
    print('Contact not found')
