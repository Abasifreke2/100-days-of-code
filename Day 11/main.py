import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_scores(card):
    """Takes a list of cards and calculates the total"""
    if len(card)== 2 and sum(card)== 21:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare_scores(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lost, Opponent has a blackjack"
    elif u_score == 0:
        return "You won with a blackjack"
    elif u_score > 21:
        return "You went over. You lost "
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"



def blackjack():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)
        print(f"Your cards: {user_cards} and current score: {user_score}")
        print(f"Computer first card:{computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal =input("Type 'y' to get another card or type 'n' to pass")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_cards !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)
    print(f"Your final hand is {user_cards} and final score is {user_score}")
    print(f"Computer's final hand is {computer_cards} and final score is {computer_score}")
    print(compare_scores(user_score,computer_score))

replay = input("Do you want to play a game of Blackjack. Type 'y' to start a new game or 'n'").lower()
if replay == "y":
    print("\n" * 20)
    blackjack()
else:
    print("Okay bye")


