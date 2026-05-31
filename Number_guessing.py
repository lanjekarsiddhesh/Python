import random

print('Welcome to the Number Guessing Game!')

Computer_number = random.randint(1, 100)
Chance = 0

while True:
    Ask_chance = int(input('How many guesses do you want: '))
    Chance += Ask_chance
    for _ in range(Ask_chance):
        Player_number = int(input('Please enter a number between 1 and 100: '))
        Chance -= 1
        print(f'You have {Chance} guesses left.')
        if Player_number < Computer_number:
            print('Too low! Try again.')
        elif Player_number > Computer_number:
            print('Too high! Try again.')
        else:
            print(f'Congratulations! You guessed the number {Computer_number}!')
            break
    print(f'Sorry, you ran out of guesses. The number was {Computer_number}.')
    break