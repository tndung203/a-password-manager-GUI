from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_list_1 = [random.choice(letters) for _ in range(nr_letters)]
    password_list_2 = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list_3 = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_list_1 + password_list_2 + password_list_3

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = em_us_entry.get()
    password = pass_entry.get()
    if len(website) != 0 and len(email) != 0 and len(password) != 0:
        is_ok = messagebox.askokcancel(title=website, message= f"These are the details entered: \nEmail: {email}"
                                                       f"\nPassword{password}\nIs it ok to save?")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website} | {email} | {password}\n")
            web_entry.delete(0,"end")
            pass_entry.delete(0, "end")
            f.close()
    else:
        messagebox.showerror(title= "Oops", message= "Please don't leave any fields empty!")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)


canvas = Canvas(width= 200, height= 200)
myimg = PhotoImage(file= "logo.png")
canvas.create_image(100,100, image=myimg)
canvas.grid(row=0, column= 1)

#Website_label
web_label = Label(text="Website:")
web_label.grid(row= 1, column= 0)

#Website_entry
web_entry = Entry(width= 35)
web_entry.grid(row = 1, column = 1, columnspan= 2)
web_entry.focus()

#Email/UserName label
em_us_label = Label(text= "Email/Username:")
em_us_label.grid(row= 2, column= 0)

#Email/Username_entry
em_us_entry = Entry(width= 35)
em_us_entry.grid(row = 2, column = 1, columnspan= 2)
em_us_entry.insert(0, "tndung922@gmail.com")

#Password_label
pass_label = Label(text="Password:")
pass_label.grid(row= 3, column= 0)

#Password_entry
pass_entry = Entry(width= 21)
pass_entry.grid(row = 3, column = 1)

#Generate_password_button
gen_passwd_button = Button(text= "Generate Password", command= generate_password)
gen_passwd_button.grid(row = 3, column = 2)

#Add_password_button
add_passwd_button = Button(text= "Add", width= 36,command= save_password)
add_passwd_button.grid(row = 4, column = 1, columnspan= 2)






window.mainloop()
