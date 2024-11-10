import pandas
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
to_learn={}
from tkinter import *
try:
    data_file = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data_file = pd.read_csv("./data/french_words.csv")
    to_learn=original_data_file.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")

random_value={}

def flip_card():
    generated_random_english = random_value["English"]
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title_text, text="English",fill="white")
    canvas.itemconfig(word_text, text=f"{generated_random_english}",fill="white")


window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer= window.after(3000,func=flip_card)



def french_word():
    global random_value,flip_timer
    window.after_cancel(flip_timer)
    random_value = random.choice(to_learn)
    generated_random_french= random_value["French"]
    canvas.itemconfig(title_text, text="French",fill="black")
    canvas.itemconfig(word_text, text=f"{generated_random_french}",fill="black")
    canvas.itemconfig(canvas_image,image=front_img)
    flip_timer=window.after(3000, func=flip_card)

def known_word():
    to_learn.remove(random_value)
    data= pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv",index=False)
    french_word()

canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_img= PhotoImage(file="./images/card_front.png")
back_img= PhotoImage(file="./images/card_back.png")
canvas_image= canvas.create_image(400,263,image=front_img)
title_text= canvas.create_text(400,150,text="",font=("Ariel",40,"italic"),fill="black")
word_text= canvas.create_text(400,263,text="",font=("Ariel",60,"bold"),fill="black")
canvas.grid(column=0,row=0,columnspan=2)

french_word()
right_img=PhotoImage(file="./images/right.png")
right=Button(image=right_img,highlightthickness=0,command=french_word)
right.grid(row=1,column=1,columnspan=2)

wrong_img= PhotoImage(file="./images/wrong.png")
wrong=Button(image=wrong_img,highlightthickness=0,command=known_word)
wrong.grid(row=1,column=0)

window.mainloop()
