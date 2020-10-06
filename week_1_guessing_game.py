from random import randint
from IPython.display import clear_output


computer_number = randint(0, 100)
guesses = 0
guessed = False

while not guessed:
    player_number = int(input('In what number am I thinking? '))
    guesses += 1
    clear_output()
    if player_number == computer_number:
        print('You took {} guesses, mofo. It is {}.'.format(guesses, computer_number))
        print('You Win!')
        break
    elif player_number > computer_number:
        print('Nope. The number is lower.')
        print('You Lose!')
    else:
        print('Nope. The number is higher.')
        print('You Lose!')