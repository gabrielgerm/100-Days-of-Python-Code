rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

options = [rock, paper, scissors]
rules = [["tie", "lose", "win"], ["win", "tie", "lose"], ["lose", "win", "tie"]]

pc_choice = random.randint(0,2)

choosen = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

if choosen == "0":
    print(f"You chose:\n{rock}\n")
    print(f"Computer chose:\n{options[pc_choice]}\n")
    print(f"You {rules[0][pc_choice]}!")
elif choosen == "1":
    print(f"You chose:\n{paper}\n")
    print(f"Computer chose:\n{options[pc_choice]}\n")
    print(f"You {rules[1][pc_choice]}!")
else:
    print(f"You chose:\n{scissors}\n")
    print(f"Computer chose:\n{options[pc_choice]}\n")
    print(f"You {rules[2][pc_choice]}!")