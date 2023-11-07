import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
            attempts += 1

            if guess < secret_number:
                print("Too low. Try again.")
            elif guess > secret_number:
                print("Too high. Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice == "yes":
        guess_the_number()
    else:
        print("Thanks for playing. Goodbye!")

if __name__ == "__main__":
    guess_the_number()
