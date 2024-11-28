from tkinter import *

# Create the main window
window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=300)
window.config(padx=50, pady=50)


def miles_to_km():
        miles = float(miles_input.get())
        km = miles * 1.60934
        answer_label.config(text=f"{km:.2f}")

# creating the input button
miles_input = Entry(width=10)
miles_input.get()
miles_input.grid(column=1, row=0)


# creating the four labels
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

equal_label = Label(text="is equal to", font=("Arial", 10))
equal_label.grid(row=1, column=0)
equal_label.config(padx=10, pady=10)

km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(row=1, column=2)
km_label.config(padx=10, pady=10)

answer_label = Label(text= "0.0", font=("Arial", 10))
answer_label.grid(row=1, column=1)
answer_label.config(padx=10, pady=10)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)
calculate_button.config(padx=2, pady=2)








window.mainloop()