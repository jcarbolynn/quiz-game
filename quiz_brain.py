class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.score = 0
    self.question_list = q_list
    
  # my attempt:(
  # def next_question(self, q_num, q_list):
  #   answer = input(f"{self.q_list[self.q_num].text}")
  #   return answer

  def next_question(self):
    current_question = self.question_list[self.question_number]
    # starts at zero
    self.question_number += 1
    user_answer = input(f"Q. {self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(user_answer, current_question.answer)

  def still_has_question(self):
    return self.question_number < len(self.question_list)
    # if self.question_number < len(self.question_list):
    #   return True
    # else:
    #   return False

    
    # if self.question_list[self.question_number] == self.question_list.length():
    #   return False
    # else:
    #   return True

  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
      self.score += 1
      print("You got it right!")
    else:
      print("You got it wrong")
    print(f"The correct answer was {correct_answer}.")
    print(f"Your current score is: {self.score}/{self.question_number}\n")
    
    
