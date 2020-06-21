import random
import time

def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two planets. In one planet, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':  # added extra cave
        print('Which planet will you go to? (1 or 2 or 3)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the planet...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 3)     # change to 3 options
    print("friendly planet is :" + str(friendlyCave))

    if chosenCave == str(friendlyCave):
         print('Chose friendly planet u survive' + str(friendlyCave))
    else:
        if chosenCave == "1":
            print('You got eaten in planet #' + chosenCave)
        elif chosenCave =='2':
            print('You got burned in planet #' + chosenCave)
        else:
            print('You got crushed in planet #' + chosenCave)

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
