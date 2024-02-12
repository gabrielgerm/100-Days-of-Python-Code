from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

def calculate():
    value = float(entry.get()) * 1.60934    
    value = round(value, 2)
    result_label.config(text=value)


# firt column
is_equal_label = Label(text="is equal to")
# label.config(font="arial 20 bold")
is_equal_label.grid(column=0,row=1)

# second column
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1,row=0)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# third column
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)





window.mainloop()