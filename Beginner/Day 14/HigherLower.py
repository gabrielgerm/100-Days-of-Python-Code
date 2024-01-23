import game_art
from game_data import data
from replit import clear
import random

def create_celebrity_B():
    celebrity_B = random.choice(data)
    while celebrity_B == celebrity_A:
        celebrity_B = random.choice(data)
    return celebrity_B

def end_game(final_score):
    clear()
    print(game_art.logo)
    print(f"Sorry, that's wrong. Final score: {final_score}")
    final_score = -1
    return final_score


celebrity_A = random.choice(data)
current_score = 0

while current_score >= 0:
    print(game_art.logo)
    if current_score > 0:
        print(f"You're right! Current score: {current_score}.")    
    celebrity_B = create_celebrity_B()
    print(f"Compare A: {celebrity_A['name']}, a {celebrity_A['description']}, from {celebrity_A['country']}.")
    print(game_art.vs)
    print(f"Against B: {celebrity_B['name']}, a {celebrity_B['description']}, from {celebrity_B['country']}.\n")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    while user_choice != 'a' and user_choice != 'b':
        user_choice = input("You don't type a possible value. Type 'A or 'B' ").lower()

    if user_choice == "a":
        if celebrity_A['follower_count'] > celebrity_B['follower_count']:
            current_score += 1
            celebrity_A = celebrity_B
            clear()
        else:
            current_score = end_game(current_score)
    else:
        if celebrity_B['follower_count'] > celebrity_A['follower_count']:
            current_score += 1
            celebrity_A = celebrity_B
            clear()
        else:
            current_score = end_game(current_score)
        
