# The clear() function will only work in the replit site
from auction_art import logo
from replit import clear

#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

yes_or_no = "yes"
bidders = {}
while yes_or_no == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()

highest_bid = 0
highest_bidder = ""
for bidder in bidders:    
    current_bid = bidders[bidder]
    if current_bid > highest_bid:
        highest_bid = current_bid
        highest_bidder = bidder      

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")