from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # column 1
        self.canvas_text = Canvas(width=300, height=250)
        self.canvas_text.create_text(150, 125, text="oiii", font=('Arial 20 italic'))
        self.canvas_text.grid(column=0, row=1, columnspan=2, pady=50)

        red_image = PhotoImage(file='./images/false.png')
        self.red_button = Button(image=red_image, highlightthickness=0, border=0)
        self.red_button.grid(column=0, row=2)

        # column 2
        self.score_label = Label(text="Score: ", bg=THEME_COLOR, fg="white", font=('Arial 12 bold'))
        self.score_label.grid(column=1, row=0)
        
        green_image = PhotoImage(file='./images/true.png')
        self.green_button = Button(image=green_image, highlightthickness=0, border=0)
        self.green_button.grid(column=1, row=2)


        self.window.mainloop()