from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)    

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(0, nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(0, nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(0, nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Field Error", message="Please fill in all fields!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\n"
                                    f"Password: {password}\n"
                                    f"Is it ok to save?")

        if is_ok:
            with open("my_logins.txt", "w") as f:
                f.write(f"{website} | {email} | {password}")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)


# Column 1
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Column 2
canvas = Canvas(width=200, height=200)
locker_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=locker_image)
canvas.grid(column=1, row=0)

website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, "gabriel-germano333@hotmail.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

add_button = Button(text="Add", width= 44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# Column 3
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)


window.mainloop()