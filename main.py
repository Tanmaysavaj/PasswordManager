import json
import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for char in range(nr_letters) ]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_list=password_letters+password_symbols+password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)





# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty.")
    else:
        is_okay = messagebox.askokcancel(
            title=website_data,
            message=f"These are the details entered: \nEmail: {email_data} \nPassword: {password_data} \nIs it okay to save?"
        )
        if is_okay:
            try:
                with open("data.json", "r") as data_file:
                    try:
                        data = json.load(data_file)
                    except json.JSONDecodeError:
                        # File is empty or invalid, start fresh
                        data = {}
            except FileNotFoundError:
                data = {}

            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data,data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Find Password ------------------------------- #
def find_password():
    website =website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file is found!")

    else:
        if website in data:
            email=data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\n password: {password}")
        else:
            messagebox.showinfo(title="Error",message="No data for entered website!")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website
website = Label(text="Website:")
website.grid(row=1, column=0)
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)

# Email
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
email_entry = Entry(width=52)
email_entry.insert(0,"tanmaysavaj@gmaail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Password
password = Label(text="Password:")
password.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", width=44,command=save)
add_button.grid(row=4, column=1, columnspan=2)





search_button = Button(text="Search",width=15,command=find_password)
search_button.grid(row=1,column=2)



window.mainloop()