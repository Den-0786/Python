from tkinter import *

# Create the main window

window = Tk()
window.title = ("Age to Days converter")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

def calculate_days():
    age = int(age_input.get())
    days = age * 365
    days_answer_label.config(text=days)
    
#Creating the input field
age_input = Entry(width=10)
age_input.get()
age_input.grid(column=1, row=0)


# Creating all the required labels

years_label = Label(text="Years", font=("Arial", 10))
years_label.grid(column=2, row=0)


is_equivalent_to_label = Label(text="Is Equivalent to", font=("Arial", 10))
is_equivalent_to_label.grid(column=0, row=1)


days_answer_label = Label(text="0", font=("Arial", 10))
days_answer_label.grid(column=1, row=1)

days_label = Label(text="Days", font=("Arial", 10))
days_label.grid(column=2, row=1)


# Creating the calculating button
calculate_days_button = Button(text="Calculate", font=("Arial", 10), command=calculate_days)
calculate_days_button.grid(column=1, row=2)



window.mainloop()