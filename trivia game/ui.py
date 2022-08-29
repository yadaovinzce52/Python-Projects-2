from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def wrong(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def right(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Trivial Hunt')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text='Score: 0')
        self.score.config(bg=THEME_COLOR, fg='white')
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Test',
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.wrong)
        self.false_button.grid(row=2, column=1)

        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.right)
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)