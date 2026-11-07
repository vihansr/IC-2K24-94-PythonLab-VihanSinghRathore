# Name: Vihan Singh Rathore
# Roll No: IC-2K24-94

contacts = {'Vihan': '9876543210', 'Rahul': '9123456780'}
name = input('Enter name to search: ')
if name in contacts:
    print('Number:', contacts[name])
else:
    print('Contact not found')
