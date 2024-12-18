import random


def generate_secret_code(length=4, characters="1234567890"):

    return ''.join(random.choices(characters, k=length))


def calculate_clues(secret, guess):

    correct_position = sum(s == g for s, g in zip(secret, guess))
    wrong_position = (
            sum(min(secret.count(ch), guess.count(ch)) for ch in set(guess)) - correct_position
    )
    return correct_position, wrong_position


def auto_mode():

    print("\nWelcome to Auto Mode!")
    print("The computer will generate a secret code. Try to guess it!\n(Note that the digits may repeat)")

    # Generate the secret code
    code_length = 4
    secret = generate_secret_code(code_length)
    max_attempts = 10

    print(f"The secret code has {code_length} digits.")

    for attempt in range(1, max_attempts + 1):
        guess = input(f"Attempt {attempt}/{max_attempts}: Enter your guess: ").strip()


        if len(guess) != code_length or not guess.isdigit():
            print(f"Invalid guess. Please enter a {code_length}-digit number.")
            continue

        correct, wrong = calculate_clues(secret, guess)
        print(f"Clue: {correct} digit(s) correct and in the right position, "
              f"{wrong} digit(s) correct but in the wrong position.")


        if correct == code_length:
            print(f"Congratulations! You guessed the secret code '{secret}' in {attempt} attempts.")
            return

    print(f"Out of attempts! The secret code was '{secret}'.")


def manual_mode():

    print("\nWelcome to Manual Mode!")
    print("Player 1 will input the secret code, and Player 2 will try to guess it!\n(Note that the digits may repeat)")


    while True:
        secret = input("Player 1: Enter the secret code (hidden from Player 2): ").strip()
        if len(secret) >= 3 and secret.isdigit():
            break
        print("Invalid input. The secret code must be at least 3 digits long and numeric.")

    print("\n" * 50)
    print("Player 2: Try to guess the secret code!")

    max_attempts = 10

    for attempt in range(1, max_attempts + 1):
        guess = input(f"Attempt {attempt}/{max_attempts}: Enter your guess: ").strip()


        if len(guess) != len(secret) or not guess.isdigit():
            print(f"Invalid guess. Please enter a {len(secret)}-digit number.")
            continue

        correct, wrong = calculate_clues(secret, guess)
        print(f"Clue: {correct} digit(s) correct and in the right position, "
              f"{wrong} digit(s) correct but in the wrong position.")


        if correct == len(secret):
            print(f"Congratulations! You guessed the secret code '{secret}' in {attempt} attempts.")
            return

    print(f"Out of attempts! The secret code was '{secret}'.")


def main():

    print("Welcome to Mastermind!")
    print("Choose a game mode:")
    print("1. Auto Mode (Computer generates the secret code)")
    print("2. Manual Mode (One player enters the secret code for another)")

    while True:
        choice = input("Enter 1 or 2 to choose your mode: ").strip()
        if choice == "1":
            auto_mode()
            break
        elif choice == "2":
            manual_mode()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()










