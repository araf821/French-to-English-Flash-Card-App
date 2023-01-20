# Goal: A flash card app that shows French words with its translation
# in English on the other side. The purpose of this app is just to
# help us learn some of the most commonly used French words.

from tkinter import *

BACKGROUND_COLOR = "#b1ddc6"

# Window init
root = Tk()
root.title("Learn French w/ Flash Cards")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Initialize images to be used in the app
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Canvas init
canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(450, 300, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# Stuff on the canvas
canvas.create_text(450, 150, text="Title", font=("gomono", 40, "italic"))
canvas.create_text(450, 263, text="WORD", font=("gomono", 60, "bold"))

# Buttons init
wrong_btn = Button(image=wrong_img, highlightthickness=0)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right_img, highlightthickness=0)
right_btn.grid(column=1, row=1)

root.mainloop()