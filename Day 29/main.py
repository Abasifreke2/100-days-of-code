from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
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
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty fields",message="Please don't leave any of the fields empty")
    else:

        is_ok = messagebox.askokcancel(title="Website",message=f"These are the details you want to save "
                                                       f"\nWebsite:{website}\nEmail:{email}\nPassword:{password}\n"
                                                       f"Press OK to save")
        if is_ok:
            with open("Saved_password.txt","a") as saved_password:
                saved_password.write(website + " | " + email+ " | " + password + "\n")
            website_entry.delete(0,END)
            password_entry.delete(0, END)
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

add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)



window.mainloop()