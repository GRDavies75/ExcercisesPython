"""
Excercise 9-57
The game of Rock, Paper & Scissors
(Rock wins from Scissors, Scissors wins from Paper, Paper wins from Rock)
The Player vs the Computer (Computer chooses random) via a menu
Display the result (win, loss, tie in case of same choice)

Made it way more elaborate and code is probably a couple of 
little changes away to change it in for example Rock, Paper, Scissors, Lizzard, Spock
"""
import random

ROCK = MINIMUM_CHOICE = 1
PAPER = 2
SCISSORS = MAXIMUM_CHOICE = 3

terms_dict = {
    ROCK: "Rock",
    PAPER: "Paper",
    SCISSORS: "Scissors",
}

choices_dict = {
    "rock": ROCK,
    "r": ROCK,
    "paper": PAPER,
    "p": PAPER,
    "scissors": SCISSORS,
    "s": SCISSORS,
}


def print_menu_header() -> None:
    print('*' * 60)
    print("The game of Rock, Paper or Scissors")
    print("You vs the Computer (randomized choice)")
    
    
def print_input_part(feedback: str='') -> None:
    print(f"{feedback}")
    print("Please type in your choice: (R)ock, (P)aper or (S)cissors")
    print("[Q = Quit]")
          

def print_computer_part(computer_choice_str: str) -> None:
    print(f"The computer has chosen: {computer_choice_str}")
    print()


def print_choices_line(player_choice_str: str, computer_choice_str: str) -> None:
    print(f"Player: {player_choice_str} vs Computer: {computer_choice_str}")


def print_result(player_choice: int, computer_choice: int) -> None:
    if player_choice == computer_choice:
        print(f"Both have chosen {terms_dict[player_choice]}")
        print("The game is a tie")
    elif (
            player_choice == ROCK and computer_choice == SCISSORS or
            player_choice == PAPER and computer_choice == ROCK or
            player_choice == SCISSORS and computer_choice == PAPER
        ):
        print_choices_line(terms_dict[player_choice], terms_dict[computer_choice])
        print("The player has won")
    else:
        print_choices_line(terms_dict[player_choice], terms_dict[computer_choice])
        print("The player has lost")
    print() # extra empty line
    

def main() -> None:
    while True: # outer loop for initializing a gameloop
        feedback_str = ''
        org_player_input = ''
        lc_player_input = ''
        player_has_chosen = None
        computer_has_chosen = None
        print_menu_header()
        while True: # inner loop for handling 1 gameplay loop
            print_input_part(feedback_str)
            org_player_input = input()
            lc_player_input = org_player_input.casefold()
            if lc_player_input == 'q':
                print("Thanks for playing")
                return # 'breaking' out of main()
            elif lc_player_input in choices_dict:
                # The game is afoot
                player_has_chosen = choices_dict[lc_player_input]
                computer_has_chosen = random.randint(MINIMUM_CHOICE, MAXIMUM_CHOICE)
                print_computer_part(terms_dict[computer_has_chosen])
                print_result(player_has_chosen, computer_has_chosen)
                break #One game play loop handled, back to the outer loop
            else:
                feedback_str = f"command {org_player_input} is not recognized"


if __name__ == "__main__":
    main()
