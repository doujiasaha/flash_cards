# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import random
import pandas

# ---------------------------- GLOBALS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
timer_var = None
spanish = ""
english = ""
wordlist = {}

# ---------------------------- DATA READING ------------------------------- #

try:
    data = pandas.read_csv("data/known_words.csv").to_dict()
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv").to_dict()
    wordlist = {original_data["spanish"][i]:original_data["english"][i] for i in original_data["spanish"]}
else:
    #Dict comprehension mapping spanish to english word
    wordlist = {data["spanish"][i]:data["english"][i] for i in data["spanish"]}

# ---------------------------- FILLING FLASH CARD ------------------------------- #

def flash_card():
    global spanish, english, timer
    window.after_cancel(timer)
    #Grab random spanish word and corresponding enlish word
        
    spanish, english = random.choice(list(wordlist.items()))
    #print(f"Selected: {spanish} -> {english}")  # Debug print
    
    canvas.itemconfig(card_image, image=front)
    canvas.itemconfig(front_language, fill="black",text=f"Spanish")
    canvas.itemconfig(front_word,fill="black",text=f"{spanish}")
    timer = window.after(3000, func=flip)

# ---------------------------- REMOVING FLASH CARD ------------------------------- #

def known():
    wordlist[spanish] = english
    print(len(wordlist))
    known_words = pandas.DataFrame(wordlist.items(), columns=["spanish","english"])
    known_words.to_csv("data/known_words.csv", index=0)
    
    del wordlist[spanish]
    flash_card()
    

# ---------------------------- FLIP FLASH CARD ------------------------------- #

def flip():
    #print(f"Selected: {spanish} -> {english}")  # Debug print
    canvas.itemconfig(card_image, image=back)
    canvas.itemconfig(front_language, fill="white",text=f"English")
    canvas.itemconfig(front_word,fill="white",text=f"{english}")

        
# ---------------------------- UI SETUP ------------------------------- #
#Basic window
window = Tk()
window.title("Flash Cards")
window.minsize(900,600)
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip)

#Canvas for cards and text within
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400,263,image=front)
front_language = canvas.create_text(400,163, text="Spanish",fill="Black",font=("arial",35,"italic"))
front_word = canvas.create_text(400,263, text="English",fill="Black",font=("arial",35,"bold"))
canvas.grid(column=0, row=0,columnspan=2)

#Wrong and correct buttons
cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image,highlightthickness=0,border=0, command=flash_card)
cross_button.grid(column=0,row=1)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image,highlightthickness=0,border=0, command=known)
check_button.grid(column=1,row=1)

flash_card()


window.mainloop()