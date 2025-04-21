from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"




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
canvas.create_image(400,263,image=front)
front_word = canvas.create_text(400,263, text="Spanish",fill="Black",font=("arial",35,"bold"))
front_text = canvas.create_text(400,163, text="English",fill="Black",font=("arial",35,"italic"))
canvas.grid(column=0, row=0,columnspan=2)

#Wrong and correct buttons
cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image,highlightthickness=0,border=0)
cross_button.grid(column=0,row=1)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image,highlightthickness=0,border=0)
check_button.grid(column=1,row=1)




window.mainloop()