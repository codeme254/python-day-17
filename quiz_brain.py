class QuizBrain:
    def __init__(self, list):
        self.q_number = 0
        self.q_list = list
        self.score = 0

    def still_has_questions(self):
        if self.q_number < len(self.q_list):
            return True
        else:
            return False
    def next_question(self):
        question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {question.text}. (True/False): ")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.q_number}\n\n")