import random

'''
Simple number guess game with Python and Random Module
There is only one tip for help and it is shown to the player 
after the first wrong guess. It shows if the number is even or odd.
It also tells if the guess it lower or higher then the number
'''


print('A simple number guessing game\n')
print('Lets see if you are lucky\n')


z = int(input('Enter number range: '))
x = random.randrange(z)

print('\n')

y = int(input('Enter a number: '))

print('\n')

firsttry = True


while (x!=y):

    print('False guess\n')

    if y>x:
        print("Make a lower guess\n")
        pass
    if y<x:
        print("Make a higher guess\n")
        pass
    
    if firsttry:
        print('Here is a quick help\n')

        if (x%2==0):
            print('It is a even number\n')
            firsttry = False
            
        else:
            print('It is an odd number\n')
            firsttry = False

    y = int(input('Enter a new number: '))
    print('\n')


if (x == y):
    print('Correct guess! YOU WIN!')
