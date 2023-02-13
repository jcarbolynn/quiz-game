from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
  question_text = question["question"]
  question_answer = question["correct_answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)


quiz = QuizBrain(question_bank)
# main loop in quizinterface like a never ending while loop, constantly checking if it needs to update something, won't work with another while loop
quiz_ui = QuizInterface(quiz)
# can specify what data type quiz_brain has to be, ensures you dont make mistakes when initializing QuizInterface

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
