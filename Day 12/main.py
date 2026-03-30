import random

LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
        51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
        71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
        91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def easy_level():
    lives = 10
    print("You have 10 attempts to guess the number")
    number = random.choice(LIST)
    while lives != 0:
        user_guess = int(input("Make a guess: "))
        if user_guess > number:
            print("Too high.\nGuess again.")
            lives -= 1
        elif user_guess < number:
            print("Too low. \nGuess again.")
            lives -= 1
        else:
            return f"You got it!. The answer was {number} "
        if lives > 0:
            print(f"You have {lives} attempt remaining")

    if lives == 0:
        print(f"You lose! The number was {number}")




def hard_level():
    lives = 5
    print("You have 5 attempts to guess the number")
    number = random.choice(LIST)
    while lives != 0:
        user_guess = int(input("Make a guess: "))
        if user_guess > number:
            print("Too high.\nGuess again.")
            lives -= 1
        elif user_guess < number:
            print("Too low.\nGuess again.")
            lives -= 1
        else:
            return f"You got it!. The answer was {number} "
        if lives > 0:
            print(f"You have {lives} attempt remaining")
    if lives == 0:
        print(f"You lose! The number was {number}")


def the_game():
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if difficulty == "easy":
        easy_level()
    if difficulty == "hard":
        hard_level()
    if difficulty != "easy" and difficulty != "hard":
        print("Please choose a correct difficulty")

the_game()