'''
Created on May 17, 2020
This is a game of rock, paper, scissors between the user and the computer.
First, the program asks the user for rock, paper, or scissors, or asks them to quit
If the user presses an incorrect key, the user will be notified that they did and ask them to try again
If the user presses quit, the software will quit
If the user presses an option for rock, paper, or scissors, the computer move will be randomly chosen.
The results will display and the user can play again until they quit.
@author: Zach George
'''
from random import choice


def get_computer_move():
    """randomly selects from rock, paper, and scissors for the computer using the choice function
    """
    move: str = choice(['rock', 'paper', 'scissors']
                       )  # set move equal to a choice between rock, paper, and scissors
    return move  # return move


def get_user_move(entry: str):
    """takes the user's entry and outputs it as rock, paper, scissors
    """
    entry = entry.upper()  # take the entry and change it to uppercase to avoid issues with case-sensitivity
    # create dictionary options, with what character equals
    options = {'R': 'rock', 'P': 'paper', 'S': 'scissors'}
    # create option string that is based off the dictionary's value of the
    # entry
    option: str = options[entry]
    return option  # return option


def get_winner(player_one: str, player_two: str):
    """outputs the winner from two string inputs for player_one and player_two
    """
    results = {('rock',
                'scissors'): 'player',
               ('rock',
                'paper'): 'computer',
               ('rock',
                'rock'): 'tie',
               ('scissors',
                'scissors'): 'tie',
               ('scissors',
                'paper'): 'player',
               ('scissors',
                'rock'): 'computer',
               ('paper',
                'scissors'): 'computer',
               ('paper',
                'paper'): 'tie',
               ('paper',
                'rock'): 'player'}  # create dictionary of player combinations and winners
    # create string of the winner from the results dictionary and player_one
    # and player_two
    winner: str = results[(player_one, player_two)]
    return winner  # return winner


def display_result(player_one: str, player_two: str):
    """displays the results based off the winner or if there was a tie
    """
    winner = get_winner(
        player_one,
        player_two)  # get the winner from player_one and player_two
    if winner == 'player':  # if the winner is the player...
        # ...print which choice beat the other and that I (the player) wins
        print(player_one + ' beats ' + player_two + '. I win!')
    elif winner == 'computer':  # if the winner is the computer...
        # ...print which choice beat the other and that you (the computer) wins
        print(player_two + ' beats ' + player_one + '. You win!')
    else:  # if there is a tie...
        # ...print the choice and that there is a tie!
        print('We both chose ' + player_one + '. It is a tie!')


def main() -> None:
    while True:  # always execute this unless Q is the entry
        # ask player for a choice and store as player_choice
        player_choice: str = input(
            'Please enter R for rock, P for paper, or S for scissors, or press Q to quit: ')
        try:  # try to execute this code based off of player_choice value
            if player_choice.upper() == 'Q':  # if the value to upper is Q...
                print('Thanks for playing!')  # ...print thanks for playing
                break  # quit the program
            else:  # if the value is not Q...
                # ...get the user's move from the player_choice
                player_choice = get_user_move(player_choice)
        except BaseException:  # execute if the try block fails
            # print that the key was incorrect and have the user try again
            print('You have entered an incorrect key. Please try again.')
        else:  # execute after try block if it succeeds and Q was not entered
            computer_choice = get_computer_move()  # get the computer's choice
            # display the winner or if there was a tie
            display_result(player_choice, computer_choice)


if __name__ == "__main__":
    main()
