# Name: Vipul Purohit
# Roll No: IC-2K24-96

import random
target = random.randint(1, 10)
print('Guess a number between 1 and 10')
while True:
    guess = int(input('Your guess: '))
    if guess == target:
        print('You got it!')
        break
    else:
        print('Wrong, try again')
