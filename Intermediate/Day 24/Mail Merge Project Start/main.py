#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter_model:
    original_letter = letter_model.read()

with open("./Input/Names/invited_names.txt") as list_names:
    people_list = list_names.readlines()

for name in range(0, len(people_list)-1):
    new_letter = original_letter.replace("[name]", people_list[name].strip())

    with open(f"./Output/ReadyToSend/{people_list[name].strip()}.txt", "w") as new_file:
        new_file.write(new_letter) 
