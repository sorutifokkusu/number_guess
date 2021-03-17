import random

'''
Simple number guess game with Python and Random Module
There is only one tip for help and it is shown to the player 
after the first wrong guess. It shows if the number is even or odd.
'''

print(' ')
print('A simple number guessing game')
print(' ')
print('Lets see if you are lucky')
print(' ')

z = int(input('Enter number range: '))
x = random.randrange(z)

print(' ')

y = int(input('Enter a number: '))

print(' ')

firsttry = True


while (x!=y):

    print('False guess')
    
    if firsttry:
        print(' ')
        print('Here is a quick help')
        print(' ')

        if (x%2==0):
            print('It is a even number')
            print(' ')
            firsttry = False
            
        else:
            print('It is an odd number')
            print(' ')
            firsttry = False

    y = int(input('Enter a new number: '))
    print(' ')


if (x == y):
    print('Correct guess! YOU WIN!')

