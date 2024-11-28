
from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox
import string
import pyperclip
import json

# ------------------------- CONSTANTS --------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ------------------------- PASSWORD GENERATOR --------------------------- #
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))
    password_entry.insert(0, password)

    pyperclip.copy(password)
# ------------------------ SAVE PASSWORD ------------------------------#

def save_password():
    website = website_entry.get()
    email   = email_entry.get()
    password = password_entry.get()
    new_data = {
            website:{
                "email":email,
                "password":password
            }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!!",message="Please make sure you fill all the fields" )
        clear_entries()
    else:
        try:
            with open("password/data.json", "r") as data_file:
            #reading the old data file
                data =json.load(data_file)
        
        except FileNotFoundError:
            with open("password/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
            messagebox.showinfo("Success", "Data saved successfully")
        else:
            # Add the new data to the existing data
            data.update(new_data)

            #Saving the updated data to the new data file
            with open("password/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            messagebox.showinfo("Success", "Information saved successfully")
        finally:
            clear_entries()
            
#------------------------- CLEARING THE ENTRIES ----------------------#
def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()
    
# ------------------------- SEARCHING FOR A PASSWORD --------------------------- #

def search():
    website = website_entry.get()
    try:
        with open("password/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
            clear_entries()
            return
        else:
            messagebox.showerror(title="Error", message=f"No details found for {website}")
# ---------------------------- UI SETUP ------------------------------#
window = Tk()
window.title("Password Generator")
window.config(padx=60, pady=40)


canvas = Canvas(window, width=250, height=250)
img = Image.open("password/logo2.jpeg")
screen_image = ImageTk.PhotoImage(img)
canvas.create_image(70, 50, image=screen_image)
canvas.grid()


# Creating the website label
website_label = Label(text="Website:", font=(FONT_NAME, 10))
canvas.create_window(5, 150, window=website_label)


website_text = StringVar()

# Function to capitalize the first letter
def capitalize_first_letter(*args):
    text = website_text.get()
    if text and text[0].islower():
        website_text.set(text[0].upper() + text[1:])

# Bind trace to call the function whenever text changes
website_text.trace_add("write", capitalize_first_letter)


# Creating the website entry
website_entry = Entry(width=20)
canvas.create_window(115, 150, window=website_entry)
website_entry.focus()

search_button = Button(text="Search", font=(FONT_NAME, 7), width=7, command=search)
canvas.create_window(205, 150, window=search_button)

# Creating the email label
email_label = Label(text="Phone/Email:", font=(FONT_NAME, 10))
canvas.create_window(5, 175, window=email_label)

# Creating the email entry
email_entry = Entry(width=29 )
canvas.create_window(140, 175, window=email_entry)
email_entry.insert(0, "dennisopokuamponsah86@gmail.com")

#Creating password label
password_label = Label(text="Password:", font=(FONT_NAME, 10))
canvas.create_window(5, 200, window=password_label)

# Creating password entry
password_entry = Entry(width=17)
canvas.create_window(105, 200, window=password_entry,)

# Creating the password generator button
password = Button(text="Generate Pwd", font=(FONT_NAME, 7), width=12, command=generate_password)
canvas.create_window(195, 200, window=password)

#Creating add button
add_button = Button(text="Add", font=(FONT_NAME, 10), width=20, command=save_password)
canvas.create_window(140, 230, window=add_button)


window.mainloop()