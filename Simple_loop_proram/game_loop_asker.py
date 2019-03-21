# src https://stackoverflow.com/questions/55273088/how-to-loop-python-game-but-also-make-it-cleaner/55274576#55274576

import random

pot = 0
number_rolls = []
winloss = [0]
valuepot = []
rollcounter = 0
maxpot = 0

def confirmation():
    user_input = input ("How much would you like to add to the pot?")
    try:
        global pot
        pot = int(user_input)
        if(pot > 0):
            valuepot.append(pot)
        else:
            print("Please enter a positive number.")
            confirmation()
    except ValueError:
        print("Please enter an integer.")
        confirmation()

def dice_roll():
    global pot
    global rollcounter
    global number_rolls
    global winloss
    global maxpot
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dicetotal = dice1 + dice2
    if pot > 0:
        if dicetotal == 7:
            pot += 4
            rollcounter += 1
            number_rolls.append(rollcounter)
            valuepot.append(pot)
            winloss.append("Win")
            if pot > maxpot:
                maxpot = pot
        dice_roll()
    elif dicetotal != 7:
        pot -= 1
        rollcounter += 1
        number_rolls.append(rollcounter)
        valuepot.append(pot)
        winloss.append("Loss")
        if pot > maxpot:
            maxpot = pot
        dice_roll()
    else:
        print("Number of rolls", '\t', "Win or Loss", '\t', "Current Value of Pot")  
        for number_rolls in number_rolls:
            print(number_rolls, '\t\t\t\t\t\t', winloss[number_rolls], '\t\t\t', valuepot[number_rolls])

def restart():
    try:
        userinput =(input('Would you like to try again? Type "yes" or "no"'))
        if userinput == ('yes'):
            confirmation()
            dice_roll()
        if userinput == ('no'):
            print("Thank you for playing, Bye-bye!")
            exit()
        else:
            print('Please type "yes" or "no"')
            return
    except ValueError:
        print('Please type "yes" or "no"')

confirmation()
dice_roll()
print('You lost your money after', rollcounter,'rolls of plays')
print('The maximum amount of money in the pot during the playing is $', maxpot)
restart()