# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

with open("nato_phonetic_alphabet.csv") as alphabet_file:
    alphabet = alphabet_file.read().split()
    alphabet_list = [letter_code.split(',')for letter_code in alphabet]
    alphabet_dictionary = {letter_code[0]:letter_code[1] for letter_code in alphabet_list}

nato_is_on = True
while nato_is_on:
    user_word = input("Type your word: ").upper().strip()
    if user_word == 'EXIT':
        nato_is_on = False
    else:
        user_response_list = [alphabet_dictionary[letter] for letter in user_word]
        print(user_response_list)
