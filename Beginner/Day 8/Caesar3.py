alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(user_text, shift_amount, direction_to_run):
    user_result = ""
    for letter in user_text:
        position = alphabet.index(letter)
        if direction_to_run == "encode":
            new_position = position + shift_amount
            user_result += alphabet[new_position]            
        else:
            new_position = position - shift_amount
            user_result += alphabet[new_position]            
    print(f"The {direction} result is {user_result}")
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(user_text=text, shift_amount=shift, direction_to_run=direction)