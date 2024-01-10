print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage_choice = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_percentage_value = total_bill*tip_percentage_choice/100
number_people = int(input("How many people to split the bill? "))

print(f"Each person shoud pay: ${(total_bill+tip_percentage_value)/number_people}")