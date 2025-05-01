import random
import time
import os

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def printf(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.1)

def get_choice(range_val):
    while True:
        choice = input(f"Enter a number between 1 and {range_val} (or 'q' to quit): ")
        if choice.lower() == 'q':
            return 'q'
        if choice.isdigit() and 1 <= int(choice) <= range_val:
            return int(choice)
        printf(f"Invalid choice. Please choose 1 to {range_val} or q.\n")

def GameStart():
    printf("Welcome to the game!\n")

def ChoiceMaker(a):
    return random.randint(1, a)

if __name__ == "__main__":
    def main():
        GameStart()
        while True:
            printf("How many hands do you want to be in the game?\nOr press q to quit\n")
            range_input = input()
            if range_input.lower() == 'q':
                printf("Goodbye!\n")
                break
            if not range_input.isdigit() or int(range_input) <= 0:
                printf("Invalid input. Please enter a positive number or 'q' to quit.\n")
                continue
            range_val = int(range_input)
            Goal = ChoiceMaker(range_val)
            user_choice = get_choice(range_val)
            if user_choice == 'q':
                printf("Goodbye!\n")
                break
            if user_choice == Goal:
                printf("You won!\n")
            else:
                printf(f"You lost! The correct number was {Goal}.\n")

    main()  # Call the main function

