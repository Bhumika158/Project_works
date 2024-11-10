from turtledemo.penrose import start

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
from tkinter import *
class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.start_score=0
        self.quiz_brain= quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        self.score = Label()
        self.score.config(text=f"Score: 0",fg="white",bg=THEME_COLOR, font=("Ariel", 10, "normal"))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250,highlightthickness=0,bg="white")
        self.que_text = self.canvas.create_text(150, 125, width=280,text="base text", font=("Ariel", 20, "italic"),fill="black")
        self.canvas.grid(column=0, row=1,columnspan=2,pady=50)

        self.right_button = Button()
        right= PhotoImage(file="images/true.png")
        self.right_button.config(image=right, highlightthickness=0,text="right",command=lambda:self.score_check("True"))
        self.right_button.grid(column=0, row=2)

        wrong=PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong,highlightthickness=0,command=lambda:self.score_check("False"))
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            questions= self.quiz_brain
            next_que= questions.next_question()
            self.canvas.itemconfig(self.que_text,text=next_que)
        else:
            self.canvas.itemconfig(self.que_text,text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def score_check(self,u_answer):
        answer= self.quiz_brain
        check_answer= answer.check_answer(u_answer)
        print(check_answer,u_answer,check_answer==u_answer)
        if check_answer==u_answer:
            self.canvas.config(bg="green")
            self.start_score += 1
            self.score.config(text=f"Score: {self.start_score}",fg="white",bg=THEME_COLOR, font=("Ariel", 10, "normal"))

        else:
            self.canvas.config(bg="red")


        self.window.after(1000,self.get_next_question)