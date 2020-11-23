"""
Author: Sanam Jena
CWID:10454295
Date: 05 Sept 2020
Objective: Implement a Rock, Paper and Scissors game where human plays against computer who randomly chooses a move.
"""

from random import choice


def get_human_move() -> str:
    """ Ask the user for R, P, or S.  Loop until given a valid input """
    while True:

        user_input1: str = input(
            "Please choose 'R', 'P', 'S' or 'Q' to quit: ")
        user_input: str = user_input1.upper()
        if user_input == "R":
            return "rock"
        elif user_input == "P":
            return "paper"
        elif user_input == "S":
            return "scissors"
        elif user_input == "Q":
            return "quit"
        else:
            print(f"You have entered {user_input1} which is invalid")
            print(
                "You can only respond using 'R' -> Rock, 'P' -> Paper, 'S' -> Scissors or 'Q' to quit")


def get_computer_move() -> str:
    """ return the computer's random choice using random.choice """
    move: str = choice(['rock', 'paper', 'scissors'])
    return move


def play_game() -> bool:
    """ play Rock/Paper/Scissors
        The human may enter 'Q' or 'q' any time to stop the game.
        Get the human's move, the computer's move, and print a message with the winner.
        Return a bool to specify if the human wants to play again,
        i.e. False when the human wants to quit or True to play again
    """
    human: str = get_human_move()
    if human == 'quit':  # human wants to quit
        return False

    computer: str = get_computer_move()

    if human == computer:
        print(f"Both human and computer have chosen {human}. It's a tie.")

    elif human == "rock":
        if computer == "paper":
            print(f"Computer has chosen {computer} & you LOST this round")
        else:
            print(f"Computer has chosen {computer} & you WON this round")
    elif human == "paper":
        if computer == "scissors":
            print(f"Computer has chosen {computer} & you LOST this round")
        else:
            print(f"Computer has chosen {computer} & you WON this round")
    elif human == "scissors":
        if computer == "rock":
            print(f"Computer has chosen {computer} & you LOST this round")
        else:
            print(f"Computer has chosen {computer} & you WON this round")

    """ TODO: your logic to determine the winner goes here """

    return True  # play again


def main() -> None:
    """ Play multiple games until the human asks to stop """
    print("Hello, Let's play Rock, Paper & Scissors")
    again: bool = True
    while again:
        again = play_game()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
