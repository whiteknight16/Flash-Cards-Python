from random import choice
import pandas
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
RANDOM = {}

# Loading a random value # Reading Data
try:
    file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    file = pandas.read_csv("./data/french_words.csv")
word_dict = file.to_dict(orient="records")


def is_known():
    word_dict.remove(RANDOM)
    data = pandas.DataFrame(word_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    loadFrench()


def loadFrench():
    global RANDOM, flip_timer
    screen.after_cancel(flip_timer)
    random_word = choice(word_dict)
    canvas.itemconfig(card_image, image=card_front_image)

    canvas.itemconfig(language, text="French", fill="Black")
    canvas.itemconfig(word, text=random_word["French"], fill="Black")
    RANDOM = random_word
    flip_timer = screen.after(3000, func=flip)


def flip():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(word, fill="White", text=RANDOM["English"])
    canvas.itemconfig(language, fill="White", text="English")


# UI
screen = Tk()
screen.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.title("Learn The new Language")
flip_timer = screen.after(3000, func=flip)
# Setting up canvas

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_right = PhotoImage(file="./images/right.png")
card_unknown = PhotoImage(file="./images/wrong.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
language = canvas.create_text(
    400, 150, text="Language", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word",
                          fill="black", font=("Ariel", 60, "bold"))

# Buttons
right = Button(image=card_right, highlightthickness=0, command=is_known)
unknown = Button(image=card_unknown, highlightthickness=0, command=loadFrench)
right.grid(row=1, column=1)
unknown.grid(row=1, column=0)

# initializing
loadFrench()

screen.mainloop()
