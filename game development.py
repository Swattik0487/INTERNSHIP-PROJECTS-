import time

def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_choice(options):
    while True:
        print("Choose an option:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def game_intro():
    print_slow("You find yourself standing in front of a mysterious cave entrance.")
    print_slow("Do you want to enter the cave or run away in fear?")
    choice = get_choice(["Enter the cave", "Run away"])
    if choice == 1:
        game_cave()
    else:
        print_slow("You ran away from the cave. Game over!")

def game_cave():
    print_slow("You enter the dark cave and see two paths.")
    print_slow("Which path will you choose?")
    choice = get_choice(["Take the left path", "Take the right path"])
    if choice == 1:
        game_left_path()
    else:
        game_right_path()

def game_left_path():
    print_slow("You walk down the left path and find a treasure chest!")
    print_slow("Congratulations, you've found a valuable treasure. You win!")
    play_again()

def game_right_path():
    print_slow("You walk down the right path and encounter a dragon!")
    print_slow("The dragon breathes fire on you. You are burned to a crisp. Game over!")

def play_again():
    choice = get_choice(["Play again", "Quit"])
    if choice == 1:
        game_intro()
    else:
        print_slow("Thanks for playing. Goodbye!")

if __name__ == "__main__":
    print_slow("Welcome to the Text Adventure Game!")
    game_intro()
