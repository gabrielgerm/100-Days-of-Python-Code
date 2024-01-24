from coffee_art import coffee, bar

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

is_off = False


def ask_user_order():
    print(coffee)
    user_order = input(f"What would you like? (espresso ${MENU["espresso"]["cost"]}/ latte ${MENU["latte"]["cost"]}/ cappuccino ${MENU["cappuccino"]["cost"]}): ")
    while user_order != "espresso" and user_order != "latte" and user_order != "cappuccino" and user_order != "resources" and  user_order != "off":
        print(f"Sorry, {user_order} is not a valid option.")
        user_order = input(f"What would you like? (espresso ${MENU["espresso"]["cost"]}/ latte ${MENU["latte"]["cost"]}/ cappuccino ${MENU["cappuccino"]["cost"]}): ")
    return user_order

def insert_coins(order):
    print("Please insert coins.")
    quartes = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    coins_value = round(quartes*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01, 2)
    if coins_value < MENU[order]["cost"]:
        print(f"Sorry, there is not enough coins. Money refunded.")
    else:
        change = round(coins_value - MENU[order]["cost"], 2)        
        if change > 0:
            resources["money"] += MENU[order]["cost"]
            print(f"Here is ${change} in change.")

        print(f"Here is your {order} ☕️. Enjoy!")


while is_off == False:
    user_order = ask_user_order()    
    
    if user_order == "espresso":
        if resources["water"] > MENU["espresso"]["ingredients"]["water"] and resources["coffee"] > MENU["espresso"]["ingredients"]["coffee"]:
            insert_coins(user_order)
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        else:
            print(f"Sorry, there is not enough ingredients")    
    elif user_order == "latte":
        if resources["water"] > MENU["latte"]["ingredients"]["water"] and resources["coffee"] > MENU["latte"]["ingredients"]["coffee"] and resources["milk"] > MENU["latte"]["ingredients"]["milk"]:
            insert_coins(user_order)
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        else:
            print(f"Sorry, there is not enough ingredients")
    elif user_order == "cappuccino":
        if resources["water"] > MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] > MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"] > MENU["cappuccino"]["ingredients"]["milk"]:
            insert_coins(user_order)
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        else:
            print(f"Sorry, there is not enough ingredients")
    elif user_order == "resources":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {resources["money"]}")
        print(bar)
    else:
        is_off = True
