#import the random module to generate random numbers
import random

print('Welcome to the Dice Rolling Game!')

#Ask to the players you want to play the game
play_game = input('Do you want to play the game? (yes/no): ')

#Ask to the players to enter their names
if play_game.lower() == 'yes':
    Player_1 = input('Player 1, please enter your name: ')
    Player_2 = input('Player 2, please enter your name: ')

def roll_dice():
    random_number = random.randint(1,6)
    return random_number

def player_1_dice(Player):
        roll = input(f'{Player}, do you want to roll the dice? (y/n): ')
        if roll.lower() == 'y':
            #generate a random number between 1 and 6 for player 1
            dice = roll_dice()
            return dice
            # Enter n/N to not roll the dice end the game.
        elif roll.lower() == 'n':
            print(f'{Player} chose not to roll the dice.')
            return None
            # Enter any other option to ask again if the player wants to roll the dice.

while play_game.lower() == 'yes':
    #Check if the players entered the names
    if Player_1 != '' and Player_2 != '':
        print(f'{Player_1} and {Player_2}, let\'s start the game!')
        
        #Ask to the player 1 to roll the dice
        dice_1 = player_1_dice(Player_1)
        print(f'{Player_1} rolled a {dice_1}.')

        #Ask to the player 2 to roll the dice
        dice_2 = player_1_dice(Player_2)
        print(f'{Player_2} rolled a {dice_2}.')

        if dice_1 is None or dice_2 is None:
            print('Game over. One of the players chose not to roll the dice.')
            break
        if dice_1 > dice_2:
            print(f'{Player_1} wins!')
        elif dice_2 > dice_1:
            print(f'{Player_2} wins!')
        else:
            print('It\'s a tie!')

    else:
        print('Please enter both player names to start the game.')
        Player_1 = input('Player 1, please enter your name: ')
        Player_2 = input('Player 2, please enter your name: ')