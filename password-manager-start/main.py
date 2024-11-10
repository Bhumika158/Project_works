
from tkinter import *
from tkinter import messagebox
import random

import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol= [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers= [random.choice(numbers) for _ in range(nr_numbers)]

    password_list= password_symbol+password_numbers+password_letter
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #   password += char
    passwordentry.insert(0,password)
    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web= websiteentry.get()
    email= emailentry.get()
    password= passwordentry.get()
    new_data = {
        web:{
            "email":email,
            "password": password
        }
    }
    if len(web)==0 or len(password)==0:
        messagebox.showinfo(title="Missing Fields",message="Please do not leave the fields empty")
    else:
        try:
            with open("data.json",mode="r") as data_file:
                data= json.load(data_file)
        except FileNotFoundError:
            with open("data.json",mode="w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json",mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            websiteentry.delete(0,END)
            passwordentry.delete(0, END)

def search_password():
    web1 = websiteentry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            try:
                available_web= data[web1]
            except KeyError:
                messagebox.showinfo(title="Oops", message="No data Available")
                websiteentry.delete(0, END)
            else:
                email=available_web["email"]
                password= available_web["password"]
                messagebox.showinfo(title="Returned", message=f"Email:{email}\n Password: {password}")
                websiteentry.delete(0, END)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data Available")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg="white")

canvas=Canvas(width=200,height=200,bg="white")
logo_img= PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website=Label()
website.config(text="Website:",fg="black",bg="white")
website.grid(column=0,row=1)


websiteentry = Entry(bg="white",width=35,fg="black")
websiteentry.grid(row=1,column=1,columnspan=3)
websiteentry.focus()

email=Label()
email.config(text="Email/Username:",fg="black",bg="white")
email.grid(column=0,row=2)

emailentry = Entry(bg="white",width=35,fg="black")
emailentry.grid(row=2,column=1,columnspan=3)
emailentry.insert(0,"bhumikapeshwani158@gmail.com")

password=Label()
password.config(text="Password:",fg="black",bg="white")
password.grid(column=0,row=3)

passwordentry = Entry(bg="white",width=23,fg="black")
passwordentry.grid(row=3,column=0,columnspan=4)


generate_button= Button()
generate_button.config(text="Generate Password",bg="white",highlightthickness=0,width=10,command=generate_password)
generate_button.grid(column=2,row=3)

Add_button= Button(bg="white",highlightthickness=0,width=32,command=save)
Add_button.config(text="Add")
Add_button.grid(column=1,columnspan=3,row=4)

search_button= Button()
search_button.config(text="Search",bg="white",highlightthickness=0,width=10,command=search_password)
search_button.grid(column=2,row=1)

window.mainloop()