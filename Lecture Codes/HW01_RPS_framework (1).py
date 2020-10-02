""" 
    Implement a Rock/Papers/Scissors game where a human plays against the computer
    who randomly chooses a move.  This solution uses only if/else statements and 
    does not use other features that we haven't discussed yet.

    Replace all of the 'TODO:' sections with your code.
"""

from random import choice

def get_human_move() -> str:
    """ Ask the user for R, P, or S.  Loop until given a valid input """
    while True:
        user_input: str = input("Please choose 'R', 'P', 'S' or 'Q' to quit: ")
        
        """ TODO: convert the user's input to 'rock', 'paper', 'scissors', 'quit' and return the string 
            Print an error message and loop again if the user inputs an invalid input value.
        """

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

    """ TODO: your logic to determine the winner goes here """

    return True  # play again

def main() -> None:
    """ Play multiple games until the human asks to stop """
    again: bool = True
    while again:
        again = play_game()
        
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
