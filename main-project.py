from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for quiz in question_data:
    question = Question(quiz["text"], quiz["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/ {len(question_bank)}")