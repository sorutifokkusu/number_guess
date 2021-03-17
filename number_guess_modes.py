import random

'''
Simple number guess game with Python and Random Module
There is only one tip for help and it is shown to the player 
after the first wrong guess. It shows if the number is even or odd.
'''

pointred = 0
lifecount = 5
point = 100


z = 0 # is an int for the randomizer
firsttry = True #For helper


#Head Comments of game
if(True):
    print(' ')
    print('A simple number guessing game')
    print(' ')
    print('Lets see if you are lucky')
    print(' ')
    print('Select a GameMode')
    print('')
    print('1. Simple | 2. Free Mode - Points | 3. Game Mode | 4. Free Mode - Points / Life')

gamemode = int(input('Selection: '))

while(gamemode > 3):
    print('Wrong selection please try again')
    print('')
    gamemode = int(input('Selection: '))

while((gamemode == 2) and (pointred == 0)):
    pointred = int(input('How many points per round do you want to lose: '))


while((gamemode == 3) and ((pointred == 0) or (lifecount == 0))):
    lifecount = 5
    pointred = 20
    print('This game mode has 20 point reduction and 5 life counts')

while((gamemode == 4) and ((pointred == 0) or (lifecount == 0))):
    pointred = int(input('How many points per round do you want to lose: '))
    lifecount = int(input('How many lives do you want in game:'))
    if(pointred == 0):
         print('Point reduction cannot be 0')
    else: 
        print('Total lives cannot be 0')

z = int(input('Enter number range: '))

if (z < 10):
    z = int(input('Enter a higher number range: '))

x = random.randrange(z)

print(' ')
y = int(input('Enter a number for guess: '))

#SIMPLE MODE
if (gamemode == 1):
    while(x!=y):
        print("False guess")

        if (firsttry):
            print("Here is a quick help")
            if (x%2==0):
                print("It is an even number")
                firsttry = False
            else:
                print("It is an odd number")
                firsttry = False
        y = int(input("Enter a new number: "))
#FREE MODE POINTS
if (gamemode == 2):
    while(x!=y):
        print("False guess")

        if (firsttry):
            print("Here is a quick help")
            if (x%2==0):
                print("It is an even number")
                firsttry = False
            else:
                print("It is an odd number")
                firsttry = False
        
        point = point - pointred
        print(point)
        print("Your current point")
        print(" ")

        y = int(input("Enter a new number: "))

        #end for gamemode 2
        if (point <=0 ):
            print('You losed')
            break
#GAME MODE
if (gamemode == 3):
    while(x!=y):
        print("False guess")

        if (firsttry):
            print("Here is a quick help")
            if (x%2==0):
                print("It is an even number")
                firsttry = False
            else:
                print("It is an odd number")
                firsttry = False
        point = point - pointred
        lifecount = lifecount - 1
        print(point , lifecount)
        print("Points / Lives left")
        
        if ((lifecount <= 0)or(point <= 0)):
            print("You lose")
            break

        y = int(input("Enter a new number: "))
#FREE MODE POINTS / LIVES
if (gamemode == 4):
    while(x!=y):
        print("False guess")

        if (firsttry):
            print("Here is a quick help")
            if (x%2==0):
                print("It is an even number")
                firsttry = False
            else:
                print("It is an odd number")
                firsttry = False
        
        point = point - pointred
        lifecount = lifecount - 1
        if ((point < 0)or(lifecount < 0)):
            print("You lose")
            break

        y = int(input("Enter a new number: "))

# END
if ((x == y) and ((lifecount>0) and (point>0))):
    print('Correct guess! YOU WIN!')

    print('Victory!')

else:
    print('Game Ends')

