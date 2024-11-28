from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#creating the screen size and the title
window = Tk()
window.title("My first GUI window")
window.minsize(width=500, height=200)
window.config(padx = 40, pady = 40)

#label for the gui
my_label = Label(text="My label", font=("Arial", 10))
my_label.config(text="Hello Dennis Opoku Amponsah,")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#creating an inout button
def show_msg():
    new_text = input.get()
    my_label.config(text= new_text)

#creating a clickable button 1
my_button = Button(text="Click Me", command=show_msg)
my_button.grid(column=1, row=1)
my_button.config(padx=10, pady=10)

#creating a clickable button 2
new_button = Button(text="New Button", command=show_msg)
new_button.grid(column=2, row=0)
new_button.config(padx=10, pady=10)


#creating an input
input = Entry(width=10)
input.get()
input.grid(column=3, row=2)










window.mainloop()