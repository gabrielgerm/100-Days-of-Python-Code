from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

def new_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(bg_image, image=card_front) 
    current_card = random.choice(list_words)

    word = current_card["English"]
    canvas.itemconfig(first_text, text="English", fill="black")
    canvas.itemconfig(second_text, text=word, fill="black")
    flip_timer = window.after(3000, flip_card) 


def flip_card():
    word = current_card["Portuguese"]
    canvas.itemconfig(first_text, text="Portuguese", fill="white")
    canvas.itemconfig(second_text, text=word, fill="white")
    canvas.itemconfig(bg_image, image=card_back)


def remove_card():
    list_words.remove(current_card)
    new_random_word()
    data = pandas.DataFrame(list_words)
    data.to_csv("./data/words_to_learn.csv", index=False)


try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/english_words.csv")
    list_words = original_data.to_dict("records")
else: 
    list_words = data.to_dict("records")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card) 

current_card = {}
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
bg_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
first_text = canvas.create_text(400, 180, text="", font=("Arial 32 italic"))
second_text = canvas.create_text(400, 280, text="", font=("Arial 38 bold"))


red_image = PhotoImage(file="./images/wrong.png")
red_button = Button(image=red_image,command=new_random_word, highlightthickness=0, borderwidth=0)
red_button.grid(column=0, row=1)

green_image = PhotoImage(file="./images/right.png")
green_button = Button(image=green_image,command=remove_card, highlightthickness=0, borderwidth=0)
green_button.grid(column=1, row=1)


new_random_word()

window.mainloop()