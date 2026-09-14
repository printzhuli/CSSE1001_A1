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
    if made > game_size:
        return 0
    return game_size + 1 - made


def valid_pokemon(guess: str, game_size: int) -> bool:
    if len(guess) != game_size or guess not in POKEMON:
        return False
    else:
        return True



def check_special_command(command: str) -> str | None:
    if command == "h" or command == "H":
        return "h"
    elif command == "q" or command == "Q":
        return "q"
    elif command == "t" or command == "T":
        return "t"
    else:
        return None


def letter_feedback(letter: str, pos: int, solution: str) -> str:
    if letter == solution[pos]:
        return GREEN
    elif letter in solution:
        return YELLOW
    else:
        return RED


def get_feedback(guess: str, solution: str) -> str:
    feedback = ""
    for pos, letter in enumerate(guess):
        feedback += letter_feedback(letter, pos, solution)
    return feedback


def strip_special_chars(guess: str) -> str:
    answer = ""
    for char in guess:
       if char in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
           answer += char
    return answer


def validate_input(command: str, game_size: int) -> str | None:
    if len(command) == 1:
        return check_special_command(command)
    else:
        stripped = strip_special_chars(command).lower()
        if valid_pokemon(stripped, game_size):
            return stripped
        else:
            return None


def get_command(game_size: int) -> str:
    while True:
        command = input(GUESS_PROMPT)
        validated = validate_input(command, game_size)
        if validated is not None:
            return validated
        


def display_guesses(
        guesses: list[str], feedback: list[str], game_size: int):
    for index, guess in enumerate(guesses):
        print(guess, feedback[index])

    empty_row = EMPTY * game_size
    for i in range(game_size + 1 - len(guesses)):
        print(f"{empty_row} {empty_row}")


def display_hint(feedback: list[str], solution: str):
    hint = [EMPTY] * len(solution)

    for pos, letter in enumerate(solution):
        guessed = False
        for guess_feedback in feedback:
            if guess_feedback[pos] == GREEN:
                guessed = True

        if not guessed:
            hint[pos] = letter
            print(" ".join(hint))
            return

    print(INVALID_HINT_MSG)


def main(sol_index: int):
    solution = get_solution(sol_index)
    game_size = get_game_size(solution)
    guesses = []
    feedback = []
    hints_remaining = game_size // 3

    print(WELCOME_MSG)

    while True:
        display_guesses(guesses, feedback, game_size)
        command = get_command(game_size)

        if command == QUIT:
            return
        elif command == HELP:
            print(HELP_MSG)
        elif command == HINT:
            if hints_remaining > 0:
                display_hint(feedback, solution)
                hints_remaining -= 1
                print(hints_remaining, REMAINING_MESSAGE)
            else:
                print(NO_HINT_MSG)
        else:
            guesses.append(command)
            feedback.append(get_feedback(command, solution))

            if command == solution:
                display_guesses(guesses, feedback, game_size)
                print(WIN_MSG)
                return
            elif guesses_remaining(len(guesses), game_size) == 0:
                display_guesses(guesses, feedback, game_size)
                print(LOSE_MSG)
                return


if __name__ == "__main__":
    # Run with your choice of Pokemon (This section is for your own testing)
    main(256)
