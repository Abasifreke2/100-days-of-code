from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "Email":email,
            "Password":password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty fields",message="Please don't leave any of the fields empty")
    else:
        try:
            with open("Saved_password.json","r") as saved_password:
                data = json.load(saved_password)
        except FileNotFoundError:
            with open("Saved_password.json", "w") as saved_password:
                json.dump(new_data,saved_password,indent=4)
        else:
            data.update(new_data)
            with open("Saved_password.json", "w") as saved_password:
                json.dump(data, saved_password, indent=4)

        website_entry.delete(0,END)
        password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("Saved_password.json", "r") as saved_password:
            data = json.load(saved_password)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data File Found")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

Email_label = Label(text="Email/Username:")
Email_label.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry.insert(0, "dummy@email.com")
email_entry.grid(column=1, row=2, columnspan=2)


Password_label = Label(text="Password:")
Password_label.grid(column=0,row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1,row=3)


generate_password = Button(text="Generate Password",command=generate_password)
generate_password.grid(column=2,row=3)

search_button= Button(text="Search",width=13,command=find_password)
search_button.grid(column=3,row=1)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)



window.mainloop()