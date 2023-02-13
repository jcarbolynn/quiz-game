from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

  def __init__(self, quiz_brain: QuizBrain): # can specify what data type quiz_brain has to be
    # to get all the questions from the particular set of 10 questions generated each time you run a game
    self.quiz = quiz_brain
    
    # self to make it a property of this class
    # self makes it accessible anywhere in the class, not done for true or false image because dont need to access it anywhere else
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)
    
    self.canvas = Canvas(width=300, height = 250, bg="white", highlightthickness=0)
    # self.question = self.canvas.create_text(150,125,text="QUESTION", fill=THEME_COLOR)
    self.question = self.canvas.create_text(
      150,
      125,
      width=280,
      text="FILLER TEXT",
      font=("Arial", 20, "italic"),
      fill=THEME_COLOR)
    self.canvas.grid(column=0,row=1,columnspan=2, pady=50)

    self.score = Label(text=f"Score: 0", font=("Arial", 12, ""), bg=THEME_COLOR, fg="white")
    self.score.grid(column=1,row=0)

    self.get_next_question()

    # in order to set the self.quiz.user_answer I have to put something into the check_answer function but that makes them both run without listening to the buttons
    # make separate functions that dont need any arguments
    true = PhotoImage(file = "images/true.png")
    self.true_button = Button(self.window, image = true, padx=20, pady=20, highlightthickness=0, command=self.true_pressed)
    self.true_button.grid(column=0,row=2)

    false = PhotoImage(file = "images/false.png")
    self.false_button = Button(self.window, image = false, padx=20, pady=20, highlightthickness=0, command=self.false_pressed)
    self.false_button.grid(column=1,row=2)


    
    self.window.mainloop()

  def get_next_question(self):
    self.canvas.config(bg="white")
    if self.quiz.still_has_questions():
      # if dont check get exception because trying to get next question even though there are none
      self.score.config(text=f"Score: {self.quiz.score}")
      q_text = self.quiz.next_question()
      # I accidentally used wrong variable name here (self.question_text), error was attribute error: 'QuizInterface' object has no attribute 'question_text'
      # it should have been self.question from when I named the text in the canvas
      # look for self.question_text in __init__
      self.canvas.itemconfig(self.question, text=q_text)
      # call get_next_question in __init__ so we do not see the filler text
    else:
      self.canvas.itemconfig(self.question, text="You finished the quiz!")
      # disable true/false buttons so the screen color doesnt change if pushed after last question asked
      self.true_button.config(state="disabled")
      self.false_button.config(state="disabled")

  def true_pressed(self):
    self.give_feedback(self.quiz.check_answer("true"))

  def false_pressed(self):
    self.give_feedback(self.quiz.check_answer("false"))

  def give_feedback(self, is_right):
    # cant use sleep because cant mess with main loop
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")

    self.window.after(1000, self.get_next_question)
