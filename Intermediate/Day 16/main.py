from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def ask_user_order():
    user_order = input(f"What would you like? (espresso / latte / cappuccino): ")
    while user_order != "espresso" and user_order != "latte" and user_order != "cappuccino" and user_order != "resources" and  user_order != "off":
        print(f"Sorry, {user_order} is not a valid option.")
        user_order = input(f"What would you like? (espresso / latte / cappuccino): ")
    return user_order   

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_off = False
while is_off == False:
    user_order = ask_user_order()
    if user_order == "resources":
        coffee_maker.report()
    elif user_order == "off":
        is_off = True
    else:
        is_possible = coffee_maker.is_resource_sufficient(menu.find_drink(user_order))
        if is_possible:
            item_cost = menu.find_drink(user_order).cost
            if money_machine.make_payment(item_cost):
                coffee_maker.make_coffee(menu.find_drink("latte"))      
        