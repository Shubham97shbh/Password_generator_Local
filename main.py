from tkinter import *
import random

windows = Tk()
color = "#FF7F27"
check_value=False
password_v = ""
index = 1
ar = []

windows.title("Password Generator")
windows.minsize(600, 350)
windows.config(padx=20, pady=20, bg=color)


def start():
    global error_w, error_u, test, check_value, password_i,password_v
    test = random.randint(11, 15)
    password_v=""
    password_val = []
    error_u = Label()
    error_u.grid(row=2, column=2)
    error_w = Label()
    error_w.grid(row=1, column=2)
    webi = web_i.get()
    if (webi[0:8] != "https://"):
        error_w.configure(text="Wrong!", bg=color, font=("Arial", 10, "bold"))
        check_value = False
    elif (webi[0:8] == "https://"):
        error_w.configure(text="            ", bg=color, font=("Arial", 10, "bold"))
        check_value = True

    useri = user_i.get()
    if (useri[len(useri) - 10:len(useri)] != "@gmail.com"):
        error_u.config(text="Wrong!", bg=color, font=("Arial", 10, "bold"))

        check_value = False
    elif (useri[len(useri) - 10:len(useri)] == "@gmail.com"):
        error_u.configure(text="            ", bg=color, font=("Arial", 10, "bold"))
        check_value = True

    string_0 = ",!@#?]"
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
    for i in password_val:
        password_v += i
    if check_value:
        password_i.delete(0,END)
        password_i.insert(0,password_v)


def Save():
    global user_i,web_i,password_v,ar,index
    if check_value:
        ar.append(f"{index}. website={web_i}\n user={user_i}\n password={password_v}\n")
        with open("./Saved_data.txt","w") as i:
            for j in ar:
                i.write(j)
                i.write("\n")
                print(j)
            index+=1



canvas = Canvas(height=180, width=200, highlightthickness=0)
lock = PhotoImage(file="./lock3.png")
canvas.create_image(50, 90, image=lock)
canvas.config(bg=color)
canvas.grid(row=0, column=1)

# website
# Text
website = Label()
website.config(text="Website :-", font=("Arial", 14, "bold"), fg="red", highlightthickness=3, bg=color)
website.grid(row=1, column=0)
# input
web_i = Entry()
web_i.config(width=60)
web_i.grid(row=1, column=1)

# email
user = Label()
user.config(text="Email/Username :-", font=("Arial", 14, "bold"), fg="red", highlightthickness=3, bg=color)
user.grid(row=2, column=0)
# input
user_i = Entry()
user_i.config(width=60)
user_i.grid(row=2, column=1)

# password
password = Label()
password.config(text="Suggested Password :-", font=("Arial", 14, "bold"), fg="green", highlightthickness=3, bg=color)
password.grid(row=3, column=0)
# genertor
password_i = Entry()
password_i.config(width=58)
password_i.grid(row=3, column=1)

password_B = Button()
password_B.config(text="Generate Password", font=("Arial", 10, "bold"), command=start)
password_B.grid(row=3, column=2)

save = Button()
save.config(text="Save", height=0, width=20, font=("Arial", 10, "bold"),command=Save)
save.grid(row=4, column=1)

windows.mainloop()
