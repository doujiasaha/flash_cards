# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import random
import pandas

# ---------------------------- GLOBALS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
timer_var = None
spanish = ""
english = ""

# ---------------------------- DATA READING ------------------------------- #

data = pandas.read_csv("data/spanish_words.csv").to_dict()

#Dict comprehension mapping spanish to english word
wordlist = {data["spanish"][i]:data["english"][i] for i in data["spanish"]}

# ---------------------------- FILLING FLASH CARD ------------------------------- #

def flash_card():
    global spanish, english
    #Grab random spanish word and corresponding enlish word    
    spanish, english = random.choice(list(wordlist.items()))
    print(f"Selected: {spanish} -> {english}")  # Debug print
    
    canvas.itemconfig(card_image, image=front)
    canvas.itemconfig(front_language, fill="black",text=f"Spanish")
    canvas.itemconfig(front_word,fill="black",text=f"{spanish}")
    countdown(3)

# ---------------------------- FLIP FLASH CARD ------------------------------- #

def flip():
    print(f"Selected: {spanish} -> {english}")  # Debug print
    canvas.itemconfig(card_image, image=back)
    canvas.itemconfig(front_language, fill="white",text=f"English")
    canvas.itemconfig(front_word,fill="white",text=f"{english}")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def countdown(count):    
    if count > 0:
            global timer_var
            timer_var = window.after(1000, countdown,count -1)
    elif count == 0:
        flip()
        
# ---------------------------- UI SETUP ------------------------------- #
#Basic window
window = Tk()
window.title("Flash Cards")
window.minsize(900,600)
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

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
check_button = Button(image=check_image,highlightthickness=0,border=0, command=flash_card)
check_button.grid(column=1,row=1)




window.mainloop()