# DO NOT modify or add any import statements
from support import *
from pokemon import POKEMON

# Name: Zhilin Chen
# Student Number: 49861161
# Least favourite Pokemon: 
# -----------------------------------------------------------------------------

# Define your classes and functions here
def get_solution(sol_index: int) -> str:
    return POKEMON[sol_index]


def get_game_size(solution: str) -> int:
    return len(solution)


def guesses_remaining(made: int, game_size: int) -> int:
    if made >= game_size:
        return 0 
    return game_size - made + 1


def valid_pokemon(guess: str, game_size: int) -> bool:
    if len(guess) != game_size or guess not in POKEMON:
        return False
    else:
        return True



def check_special_command(command: str) -> str | None:
    if command in "hH":
        return "h"
    elif command in "qQ":
        return "q"
    elif command in "tT":
        return "t"
    else:
        return None


def letter_feedback(letter: str, pos: int, solution: str) -> str:
    pass


def get_feedback(guess: str, solution: str) -> str:
    pass


def strip_special_chars(guess: str) -> str:
    pass


def validate_input(command: str, game_size: int) -> str | None:
    pass


def get_command(game_size: int) -> str:
    pass


def display_guesses(
        guesses: list[str], feedback: list[str], game_size: int):
    pass


def display_hint(feedback: list[str], solution: str):
    pass


def main(sol_index: int):
    pass

if __name__ == "__main__":
    # Run with your choice of Pokemon (This section is for your own testing)
    print(get_solution(1))

