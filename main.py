from tkinter import *
# only import classes and variable not the method
from tkinter import messagebox
import random
import pyperclip
import json

windows = Tk()
#bgcolor
color = "#FF7F27"

check_value = False
password_v = ""
index = 1
ar = []

windows.title("Password Generator")
windows.minsize(650, 350)
windows.config(padx=20, pady=20, bg=color)


def start():
    global error_w, error_u, test, check_value, password_i, password_v
    check_value = 0
    test = random.randint(11, 15)
    password_v = ""
    password_val = []
    error_u = Label()
    error_u.grid(row=2, column=3, columnspan=2)
    error_w = Label()
    error_w.grid(row=1, column=3, columnspan=2)
    webi = web_i.get()
#user error check -----------------------------------------------------------------------------------------------------
    if (webi[0:8] != "https://"):
        error_w.configure(text="Wrong!", bg=color, font=("Arial", 10, "bold"))
        check_value = 0
    elif (webi[0:8] == "https://"):
        error_w.configure(text="            ", bg=color, font=("Arial", 10, "bold"))
        check_value += 1

    useri = user_i.get()
    if (useri[len(useri) - 10:len(useri)] != "@gmail.com"):
        error_u.config(text="Wrong!", bg=color, font=("Arial", 10, "bold"))
        check_value = 0
    elif (useri[len(useri) - 10:len(useri)] == "@gmail.com"):
        error_u.configure(text="            ", bg=color, font=("Arial", 10, "bold"))
        check_value += 1
#password generator----------------------------------------------------------------------------------------------------
    string_0 = "!@#?$"
    string_1 = "abcdelghijklmnopqrstuvwxyz"
    string_2 = "0123456789"
    while test != 0:
        rand = random.randint(0, 8)
        if rand == 0 or rand == 7:
            password_val.append(random.choice(string_0))
        elif rand == 2 or rand == 4 or rand == 5:
            password_val.append(random.choice(string_1))
        elif rand == 1 or rand == 3:
            password_val.append(random.choice(string_1.upper()))
        elif rand == 6:
            password_val.append(random.choice(string_2))
        test -= 1
    password_v = "".join(password_val)
#pasword upload -------------------------------------------------------------------------------------------------------
    if check_value == 2:
        password_i.delete(0, END)
        password_i.insert(0, password_v)
        pyperclip.copy(password_v)


def Save():
    global check_value, user_i, web_i, password_v
# format for saving a dictionary---------------------------------------------------------------------------------------
    new_data = {
        web_i.get():
            {"user": user_i.get(), "password": password_v}
    }
    if check_value == 2:
        try:
            with open("data.json", "r") as data_l:
                data = json.load(data_l)
        except FileNotFoundError:
            with open("data.json", "w") as data_l:
                json.dump(new_data, data_l, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_l:
                json.dump(data, data_l, indent=4)
        finally:
            password_i.delete(0, END)
            web_i.delete(0, END)
            user_i.delete(0, END)
            check_value = 0
    else:
        messagebox.showinfo(title="ERROR", message="Your fields are empty or wrong input, fail to save!")


# search
def search():
    check_website = web_i.get()
    try:
        with open("data.json") as data:
            data_o = json.load(data)
            user_o = data_o[check_website]["user"]
            password_o = data_o[check_website]["password"]
        pyperclip.copy(password_o)
        messagebox.showinfo(title=check_website, message=f"Email={user_o}\nPassword={password_o}")
    except KeyError:
        messagebox.showinfo(title="ERROR", message=f"No Stored Data, Save it first")
    except FileNotFoundError:
        messagebox.showinfo(text="ERROR",message="Nothing file is saved")
#image layout format---------------------------------------------------------------------------------------------------
canvas = Canvas(height=180, width=200, highlightthickness=0)
lock = PhotoImage(file="./lock3.png")
canvas.create_image(50, 90, image=lock)
canvas.config(bg=color)
canvas.grid(row=0, column=1)

# website
# Text
website = Label()
website.config(text="Website :-", font=("Arial", 14, "bold"), fg="#0029FF", highlightthickness=3, bg=color)
website.focus()
website.grid(row=1, column=0)
# input
web_i = Entry()
web_i.config(width=32)
web_i.grid(row=1, column=1)
# button
search_com = Button()
search_com.config(text="search", height=0, width=18, font=("Arial", 9, "bold"), command=search)
search_com.grid(row=1, column=2)

# email
user = Label()
user.config(text="Email/Username :-", font=("Arial", 14, "bold"), fg="#0029FF", highlightthickness=3, bg=color)
user.grid(row=2, column=0)
# input
user_i = Entry()
user_i.config(width=57)
user_i.grid(row=2, column=1, columnspan=2)

# password
password = Label()
password.config(text="Suggested Password :-", font=("Arial", 14, "bold"), fg="green", highlightthickness=3, bg=color)
password.grid(row=3, column=0)
# genertor
password_i = Entry()
password_i.config(width=32)
password_i.grid(row=3, column=1)

password_B = Button()
password_B.config(text="Generate Password", width=20, font=("Arial", 9, "bold"), command=start)
password_B.grid(row=3, column=2)

save = Button()
save.config(text="Save", height=0, width=10, font=("Arial", 9, "bold"), command=Save)
save.grid(row=4, column=1)

windows.mainloop()
