
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer1=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer1)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_sec=WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN*60
    long_break_sec= LONG_BREAK_MIN*60
    global reps
    reps+=1
    if reps == 8:
        timer.config(text="Long_Break",fg=RED)
        countdown(long_break_sec)
    elif reps%2==0:
        timer.config(text="Short_Break",fg=PINK)
        countdown(short_break_sec)
    else:
        timer.config(text="Work",fg=GREEN)
        countdown(work_sec)
# ---------------------------- 1COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min= count // 60
    count_sec= count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer1
        timer1=window.after(1000,countdown, count-1)
    else:
        start_timer()
        mark=""
        worksessions= math.floor(reps/2)
        for _ in range(worksessions):
            mark+="✔"
        checkmark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


timer=Label()
timer.config(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,40,"normal"))
timer.grid(column=2,row=1)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text= canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

def hit_start():
    start_timer()

start_button= Button()
start_button.config(text="Start",bg=YELLOW,highlightthickness=0,command=hit_start)
start_button.grid(column=1,row=3)

reset_button= Button(bg=YELLOW,highlightthickness=0,command=reset_timer)
reset_button.config(text="Reset")
reset_button.grid(column=3,row=3)

checkmark= Label(bg=YELLOW,fg=GREEN)
checkmark.grid(column=2,row=4)



window.mainloop()