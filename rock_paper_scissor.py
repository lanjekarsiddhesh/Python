import random

Game_object = ['r', 'p', 's']
emojis = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}

print('Welcome to the Rock, Paper, Scissor Game!')

# Ask the players if they want to play the game
Ask_for_game = input('Do you want to play the game? (yes/no): ')

# Define a function to determine the winner of the game based on the choices of both players
def play_game(Player_1_choice, Player_2_choice,Player_1_Name, Player_2_Name):
    if Player_1_choice.lower() == 'r' and Player_2_choice == 'r':
        print(f'{Player_1_Name} choose rock {emojis[Player_1_choice.lower()]}\n{Player_2_Name} choose rock {emojis[Player_2_choice.lower()]}\nIt\'s a tie!')
        print('-----------------------------------------------------------------------------------------------------------')
    elif Player_1_choice.lower() == 'r' and Player_2_choice == 's':
        print(f'{Player_1_Name} choose rock {emojis[Player_1_choice.lower()]}\n{Player_2_Name} choose scissor {emojis[Player_2_choice.lower()]}\n{Player_1_Name} wins!')
        print('-----------------------------------------------------------------------------------------------------------')
    elif Player_1_choice.lower() == 'r' and Player_2_choice == 'p':
        print(f'{Player_1_Name} choose rock {emojis[Player_1_choice.lower()]}\n{Player_2_Name} choose paper {emojis[Player_2_choice.lower()]}\n{Player_2_Name} wins!')
        print('-----------------------------------------------------------------------------------------------------------')

    elif Player_1_choice.lower() == 'p' and Player_2_choice == 'p':
        print(f'{Player_1_Name} choose paper {emojis[Player_1_choice.lower()]}\n{Player_2_Name} choose paper {emojis[Player_2_choice.lower()]}\nIt\'s a tie!')
        print('-----------------------------------------------------------------------------------------------------------')
    elif Player_1_choice.lower() == 'p' and Player_2_choice == 's':
        print(f'{Player_1_Name} choose paper {emojis[Player_1_choice.lower()]}\n{Player_2_Name} choose scissor {emojis[Player_2_choice.lower()]}\n{Player_2_Name} wins!')
        print('-----------------------------------------------------------------------------------------------------------')
    elif Player_1_choice.lower() == 'p' and Player_2_choice == 'r':
        print(f'{Player_1_Name} choose paper {emojis[Player_1_choice.lower()]}\n{Player_2_Name} choose rock {emojis[Player_2_choice.lower()]}\n{Player_1_Name} wins!')
        print('-----------------------------------------------------------------------------------------------------------')

    elif Player_1_choice.lower() == 's' and Player_2_choice == 's':
        print(f'{Player_1_Name} choose scissor {emojis[Player_1_choice.lower()]}\n{Player_2_Name} choose scissor {emojis[Player_2_choice.lower()]}\nIt\'s a tie!')
        print('-----------------------------------------------------------------------------------------------------------')
    elif Player_1_choice.lower() == 's' and Player_2_choice == 'p':
        print(f'{Player_1_Name} choose scissor {emojis[Player_1_choice.lower()]}\n{Player_2_Name} choose paper {emojis[Player_2_choice.lower()]}\n{Player_1_Name} wins!')
        print('-----------------------------------------------------------------------------------------------------------')
    elif Player_1_choice.lower() == 's' and Player_2_choice == 'r':
        print(f'{Player_1_Name} choose scissor {emojis[Player_1_choice.lower()]}\n{Player_2_Name} choose rock {emojis[Player_2_choice.lower()]}\n{Player_2_Name} wins!')
        print('-----------------------------------------------------------------------------------------------------------')

    else:
        print(f'Invalid choice. Please choose rock {emojis["r"]} -> r, paper {emojis["p"]} -> p, scissor {emojis["s"]} -> s.')
        print('-----------------------------------------------------------------------------------------------------------')


if Ask_for_game.lower() == 'yes':

    # Ask the player if they want to play against the computer or another player
    Choose_opponent = input('Do you want to play against the computer or player? (computer[C]/player[P]): ')
    print('-----------------------------------------------------------------------------------------------------------')

    # Ask the player how many rounds they want to play
    Ask_for_count = int(input('How many rounds do you want to play? '))
    print('-----------------------------------------------------------------------------------------------------------')

    # If the player chooses to play against the computer, ask for their name and start the game
    if Choose_opponent.lower() == 'c' or Choose_opponent.lower() == 'computer':

        print('You have choosen to play against the computer.')

        # Ask the player to enter their name
        Ask_player_name = input('Please enter your name: ')
        print(f'Hello {Ask_player_name}, let\'s start the game!')
        print('-----------------------------------------------------------------------------------------------------------')

        while True:
            try:

                if Ask_for_count > 0:

                    # Loop through the number of rounds and play the game until the rounds are over
                    for _ in range(Ask_for_count):

                        # Ask the player to choose rock, paper, or scissor and generate a random choice for the computer
                        Player_1_choice = input(f'Please choose rock {emojis["r"]}-> r, paper {emojis["p"]} -> p, scissor {emojis["s"]} -> s: ')

                        # Generate a random choice for the computer
                        Player_2_choice = random.choice(Game_object)

                        # Play the game and determine the winner
                        play_game(Player_1_choice=Player_1_choice, Player_2_choice=Player_2_choice, Player_1_Name=Ask_player_name, Player_2_Name='Computer')

                        # Decrease the round count and display the remaining rounds
                        Ask_for_count -= 1
                        print(f'You have {Ask_for_count} rounds left.')
                        print('-----------------------------------------------------------------------------------------------------------')
                    
                    # Once the rounds are over, display a game over message and break the loop
                    if Ask_for_count == 0:
                        print('Game over. Thanks for playing!')
                        print('----------END----------END----------END----------END----------END----------END----------END----------END----------END----------END----------')
                        break

            except ValueError:
                print('Invalid input. Please enter a valid number.')
                print('-----------------------------------------------------------------------------------------------------------')

    # If the player chooses to play against another player, ask for both players' names and start the game
    elif Choose_opponent.lower() == 'p' or Choose_opponent.lower() == 'player':
        print('You have choosen to play against another player.')
        print('-----------------------------------------------------------------------------------------------------------')

        # Ask both players to enter their names
        Ask_player_1 = input('Player 1, please enter your name: ')
        print('-----------------------------------------------------------------------------------------------------------')
        Ask_player_2 = input('Player 2, please enter your name: ')
        print('-----------------------------------------------------------------------------------------------------------')
        print(f'Hello {Ask_player_1} and {Ask_player_2}, let\'s start the game!')
        print('-----------------------------------------------------------------------------------------------------------')

        while True:
            try:

                if Ask_for_count > 0:

                    # Loop through the number of rounds and play the game until the rounds are over
                    for _ in range(Ask_for_count):

                        # Ask both players to choose rock, paper, or scissor
                        Player_1_choice = input(f'{Ask_player_1}, please choose rock {emojis["r"]}-> r, paper {emojis["p"]} -> p, scissor {emojis["s"]} -> s: ')
                        Player_2_choice = input(f'{Ask_player_2}, please choose rock {emojis["r"]}-> r, paper {emojis["p"]} -> p, scissor {emojis["s"]} -> s: ')

                        # Play the game and determine the winner
                        play_game(Player_1_choice=Player_1_choice, Player_2_choice=Player_2_choice, Player_1_Name=Ask_player_1, Player_2_Name=Ask_player_2)

                        # Decrease the round count and display the remaining rounds
                        Ask_for_count -= 1
                        print(f'You have {Ask_for_count} rounds left.')
                        print('-----------------------------------------------------------------------------------------------------------')

                    # Once the rounds are over, display a game over message and break the loop
                    if Ask_for_count == 0:
                        print('Game over. Thanks for playing!')
                        print('----------END----------END----------END----------END----------END----------END----------END----------END----------END----------END----------')
                        break

            except ValueError:
                print('Invalid input. Please enter a valid number.')
                print('-----------------------------------------------------------------------------------------------------------')
else:
    print('Maybe next time!')
    print('----------END----------END----------END----------END----------END----------END----------END----------END----------END----------END----------')




