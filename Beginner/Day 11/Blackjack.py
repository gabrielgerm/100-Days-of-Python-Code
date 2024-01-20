import random
from replit import clear
from art import logo


all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
have_ace = False

my_hand = []
my_score = 0
my_status = ""
computer_hand = []
computer_score = 0
computer_status = ""


def give_card(hand):
    hand.append(all_cards[random.randint(0, 12)])


def have_ace():
    for card in my_hand:
        if card == 11:
            return True
    return False


def ask_another_card():
        give_card(my_hand)
        my_score = sum(my_hand)


def check_my_score():
    my_score = sum(my_hand)
    if my_score == 21:
        my_status = "win"
    else:
        if my_score > 21:
            if have_ace():
                my_hand[my_hand.index(11)] = 1
                my_score = sum(my_hand)
                if my_score > 21:
                    my_status = "lose"
                elif my_score == 21:
                    my_status = "win"
                else:
                    if input("Type 'y' to get another card, Type 'n' to pass: ") == "y":
                        ask_another_card()
                        print(f"    Your cards: {my_hand}, current score: {my_score}")
                        check_my_score()
            else:
                my_status = "lose"
        else:
            if input("Type 'y' to get another card, Type 'n' to pass: ") == "y":
                ask_another_card()
                print(f"    Your cards: {my_hand}, current score: {my_score}")
                check_my_score()

def check_computer_score():
    computer_score = sum(computer_hand)
    while computer_score < 17:    
        give_card(computer_hand)
        computer_score = sum(computer_hand)
    if computer_score == 21:
        computer_status = "win"
    elif computer_score > 21:
        if have_ace():
            computer_hand[computer_hand.index(11)] = 1
            computer_score = sum(computer_hand)
            if computer_score > 21:
                computer_status = "lose"
            elif computer_score == 21:
                computer_status = "win"
            else:
                if computer_score < 17:
                    check_computer_score()














if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":

    clear()
    print(logo)


    give_card(my_hand)
    give_card(my_hand)
    my_score = sum(my_hand)

    give_card(computer_hand)
    give_card(computer_hand)
    computer_score = sum(computer_hand)

    print(f"    Your cards: {my_hand}, current score: {my_score}")
    print(f"    Computer's first card: {computer_hand[0]}")

    check_my_score()
    check_computer_score()

    print(f"    Your cards: {my_hand}, current score: {my_score}")
    print(f"    Computer's cards: {computer_hand}, computer's score: {computer_score}")

    if my_status == "win":
        if computer_status == "win":
            print('draw')
        elif computer_status == "lose":
            print('you win')

    elif my_status == "lose":
        if computer_status == "win":
            print('you lose')
        elif computer_status == "lose":
            print('draw')

    elif my_status == "":
        if computer_status == "win":
            print('you lose')
        elif computer_status == "lose":
            print('you win')
        else:
            if my_score > computer_score:
                print('you win')
            elif my_score < computer_score:
                print('you lose')
            else:
                print('draw')
