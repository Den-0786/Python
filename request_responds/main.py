from tkinter import *
from PIL import Image, ImageTk
import requests


#------------------Quote Function --------------------#
def get_quote():
    # Get a quote from the API
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

#-------------------UI SETUP -------------------------#
window = Tk()
window.title("Kanye Quote")
window.config(padx=20, pady=20)


# Creating the image window
canvas = Canvas(window, width=400, height=400)
img = Image.open("request_responds/download.png")
quote_img = ImageTk.PhotoImage(img)
canvas.create_image(150, 150, image=quote_img)
quote_text = canvas.create_text(150, 150, text="", width=300, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Creating the image for the kanye

kanye_img = Image.open("request_responds/kanye.png")
kanye_img = kanye_img.resize((50, 50))
kanye_photo = ImageTk.PhotoImage(kanye_img)
kanye_button = Button(image=kanye_photo, highlightthickness=0, command=get_quote)
canvas.create_window(160, 335,window=kanye_button)


window.mainloop()
