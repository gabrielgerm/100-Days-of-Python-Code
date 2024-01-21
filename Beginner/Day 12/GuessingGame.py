from guess_game_art import logo
from replit import clear
import random

def guess_loop(attempts):
    have_win = False
    while attempts > 0 and have_win == False:        
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))
        attempts -= 1

        if guessed_number > CORRECT_GUESS:
            print("Too high.")
        elif guessed_number < CORRECT_GUESS:
            print("Too low.")  
        else:
            print(f"You got it! The answer was {CORRECT_GUESS}.")
            have_win = True

    if attempts == 0 and have_win == False:
        print("You've run out of guesses, you lose.")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
CORRECT_GUESS = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
while difficulty != "easy" and difficulty != "hard":
    difficulty = input("You don't type a option. Type 'easy' or 'hard': ")
clear()

if difficulty == "easy":
    guess_loop(10)
else:
    guess_loop(5)