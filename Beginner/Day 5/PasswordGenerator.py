#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# final_response = ""
# for letter in range(0, nr_letters):
#     final_response += letters[random.randint(0, len(letters)-1)]

# for symbol in range(0, nr_symbols):
#     final_response += symbols[random.randint(0, len(symbols)-1)]
    
# for number in range(0, nr_numbers):
#     final_response += numbers[random.randint(0, len(numbers)-1)]

# print(final_response)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

final_response = ""
for letter in range(0, nr_letters):
    final_response += letters[random.randint(0, len(letters)-1)]

for symbol in range(0, nr_symbols):
    final_response += symbols[random.randint(0, len(symbols)-1)]

for number in range(0, nr_numbers):
    final_response += numbers[random.randint(0, len(numbers)-1)]

final_response_list = list(final_response)
random.shuffle(final_response_list)
final_response = "".join(final_response_list)
print(final_response)