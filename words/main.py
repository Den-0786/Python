from tkinter import *
from PIL import Image, ImageTk
import random
import pandas
import time
BACKGROUND_COLOR = "#B1DDC6"
current_card = []
to_learn = []

try:
    data = pandas.read_csv("words/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")

except FileNotFoundError:
    original_data = pandas.read_csv("words/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global to_learn, current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)

def right_answer():
    global to_learn, current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words/words_to_learn.csv", index=False)
    next_card()
    

window = Tk()
window.title("Flashy")
window.config(padx=0, pady=0)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=300, height=320, bg=BACKGROUND_COLOR)
canvas.grid()

front_card = Image.open("words/card_front.png")
front_card = front_card.resize((280, 200))
front_image = ImageTk.PhotoImage(front_card)
card_background = canvas.create_image(150, 130, image=front_image)
card_title = canvas.create_text(150, 80, font=("Arial", 20, "italic"))
card_word = canvas.create_text(150, 150, font=("Arial", 30, "bold"))

back_card = Image.open("words/card_back.png")
back_card = back_card.resize((280, 200))
back_image = ImageTk.PhotoImage(back_card)


img2 = Image.open("words/wrong.png")
img2 = img2.resize((50, 50))
unknown_image = ImageTk.PhotoImage(img2)
unknown_button = Button(window, image=unknown_image, borderwidth=0, highlightthickness=0, command=next_card)
unknown_button.place(x=30, y=260)

img = Image.open("words/right.png")
img = img.resize((50, 50))
check_image = ImageTk.PhotoImage(img)
known_button = Button(window, image=check_image, borderwidth=0, highlightthickness=0, command=right_answer)
known_button.place(x=210, y=260)


next_card()


window.mainloop()