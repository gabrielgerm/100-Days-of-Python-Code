from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)


quizgame = QuizzBrain(question_bank)
while quizgame.still_has_questions():
    quizgame.next_question()
print(f"You've completed the quiz game!\nYour final score is {quizgame.score}/{len(question_bank)}")