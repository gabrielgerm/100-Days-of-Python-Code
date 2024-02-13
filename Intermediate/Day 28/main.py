from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps%8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps%2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    else:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):    
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(3, count_down, count-1)
    else:
        start_timer()
        check_marks = ''
        for _ in range(0, math.floor(reps/2)):
            check_marks += "✔"
        check_label.config(text=check_marks)

        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)                   

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_image)
timer_text = canvas.create_text(100, 133, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
check_label.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()