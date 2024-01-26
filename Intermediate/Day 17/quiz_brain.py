class QuizzBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question_number = self.question_number
        self.question_number += 1  
        print(f"Q.{self.question_number} {self.question_list[current_question_number].question}")
        user_answer = input("Your answer? (True or False): ")
        self.check_answer(user_answer, current_question_number)
        

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, current_question_number):
        correct_answer = self.question_list[current_question_number].correct_answer     
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else: 
            print("Wrong!")
        print(f"The correrct answer was: {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_number}\n")