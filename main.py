from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# q1 = Question(question_data[0]["text"], question_data[0]["answer"])
# print(q1.text)
# print(q1.answer)

# print(len(question_data))
# q2 = Question(question_data[0]["text"], question_data[0]["answer"])
# print(q2.answer)

question_bank = []
# for index in range(len(question_data)):
#   for key, value in question_data:
#     title = "q" + str(index)
#     title = Question(question_data[index][key], question_data[index][value])
#     question_bank.append(title)

# convert each pieces of data with string keys (easy to make mistakes) and converting to object which has all the data in an easy and foolproof way of accessing
for question in question_data:
  question_text = question["text"]
  question_answer = question["answer"]
  # q_text and q_answer come from question_model
  new_question = Question(q_text = question_text, q_answer = question_answer)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
  quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
