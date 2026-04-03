#import the necessary files
import random
from art import logo
from art import vs
from game_data import data
#Randomly select a key from a dictionary in a list
A = random.choice(data)
B = random.choice(data)
highest_follower = 0
score = 0
#Create two variables A and B
#Compare between A and B
#Then store the highest in a variable
is_game_running = True
while is_game_running:
    if A['follower_count'] < B['follower_count']:
        highest_follower = A['follower_count']
    else:
        highest_follower = B['follower_count']
    first_celebrity = f"{A['name']}, a {A['description']}, from {A['country']} "
    second_celebrity = f"{B['name']}, a {B['description']}, from {B['country']}"
    print(logo)
    print(f"Compare A :{first_celebrity} ")
    print(vs)
    print(f"Against B : {second_celebrity}")
    #Ask for user to pick between A and B
    user_choice = input("Who has more followers. Type 'A' or 'B': ").upper()
    #if user choice is equal to something and the variable is equal to the highest then the highest becomes the new A
    if user_choice == "A" and highest_follower == A['follower_count']:
        score += 1
        print(f"You're right! Current Score: {score}")
        A = A
        B = random.choice(data)
        print("\n" * 20)
    elif user_choice == "B" and highest_follower == B['follower_count']:
        score += 1
        print(f"You're right! Current Score: {score}")
        A = B
        B = random.choice(data)
        print("\n" * 20)
    elif user_choice != "A" and user_choice != "B":
        print("Invalid input. Please type A or B.")
        is_game_running = False
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        is_game_running = False
