import random
from tkinter import *
import pandas as pd
import json

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- Pandas list from CSV ------------------------------- #
french_words = pd.read_csv("french_words.csv")
data_frame = pd.DataFrame(french_words)
french_words = data_frame.to_dict(orient="records")
print(french_words)

# ---------------------------- Create new Flash Cards ------------------------------- #
count = 0
words = ""
random_int = 0
english_words = ""
fren_word = ""


def change_card_wrong():
    global count
    global words
    global random_int
    global english_words
    global fren_word
    to_learn = french_words[random_int]
    with open("words_to_learn.json", "a") as file:
        json.dump(to_learn, file, indent=4)
    new_card()


def change_card():
    global count
    global words
    global random_int
    global english_words
    global fren_word
    if count == 1:
        canvas.itemconfig(card, image=card_back)
        canvas.itemconfig(language, text="English")
        canvas.itemconfig(word, text=english_words)
        count -= 1
    else:
        canvas.itemconfig(card, image=card_front)
        canvas.itemconfig(language, text="French")
        canvas.itemconfig(word, text=word)


def new_card():
    global words
    global count
    global random_int
    global english_words
    global fren_word
    change_card()
    random_int = random.randint(1, len(french_words))
    count += 1
    fren_words = french_words[random_int]["French"]
    english_words = french_words[random_int]["English"]
    canvas.itemconfig(word, text=fren_words)
    window.after(3000, change_card)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Cards
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
card_front_text = 'Black'
card_back_text = "white"
card = canvas.create_image(400, 265, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
language = canvas.create_text(400, 150, text="French", fill="black", font="Arial 40 italic")
word = canvas.create_text(400, 263, text="Word", fill="black", font="Arial 60 bold")

# Buttons
right = PhotoImage(file="right.png")
button_right = Button(image=right, highlightthickness=0, height=90, width=90, command=new_card)
button_right.grid(column=1, row=1)

wrong = PhotoImage(file="wrong.png")
button_wrong = Button(image=wrong, highlightthickness=0, height=90, width=90, command=change_card_wrong)
button_wrong.grid(column=0, row=1)

window.mainloop()
