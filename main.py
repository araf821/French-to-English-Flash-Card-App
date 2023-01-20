# Goal: A flash card app that shows French words with its translation
# in English on the other side. The purpose of this app is just to
# help us learn some of the most commonly used French words.

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#b1ddc6"
# This global variable keeps track of a random work from our dictionary
random_word = ""

# Window init
root = Tk()
root.title("Learn French w/ Flash Cards")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Initialize images to be used in the app
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Generating the disctionary from a csv file
df = pandas.read_csv("data/french_words.csv")
dictionary = df.to_dict(orient="records")

# Generates a random french word
def generate_random():
    # Flip card to show the front of the card
    canvas.itemconfig(card_img, image=card_front_img)

    global random_word
    random_word = random.choice(dictionary)
    french_word = random_word["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=french_word)
    
# Flips the card to show the translation of the french word
def show_english():
    # Flip card to show the back of the card
    canvas.itemconfig(card_img, image=card_back_img)

    eng_word = random_word["English"]
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=eng_word)

# Canvas init
canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(450, 300, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# Stuff on the canvas
card_title = canvas.create_text(450, 150, text="Title", font=("gomono", 40, "italic"))
card_word = canvas.create_text(450, 263, text="word", font=("gomono", 60, "bold"))

# Buttons init
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=show_english)
wrong_btn.grid(column=0, row=1)
right_btn = Button(image=right_img, highlightthickness=0, command=generate_random)
right_btn.grid(column=1, row=1)

# This function gets called when the app first runs
generate_random()

root.mainloop()