class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer

class QuizBrain:

    def __init__(self,questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)


    def still_has_quesitons(self):
        if self.question_number >= 12:
            return False
        else:
            return True

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print ("You got it right!")
            self.score += 1
            print(f"{self.score}/{self.question_number}")
        else:
            print("You got it wrong!")
            print(f"{self.score}/{self.question_number}")
        print(f"The correct answer is {correct_answer}")
        print("\n")


question_data = [
    {"category": "Entertainment: Film",
     "type": "boolean",
     "difficulty": "easy",
     "question": "The movie The Nightmare before Christmas was all done with physical objects.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "Matt Damon played an astronaut stranded on an extraterrestrial planet in both of the movies Interstellar and The Martian.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "The 2010 film The Social Network is a biographical drama film about MySpace founder Tom Anderson.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "The word Inception came from the 2010 blockbuster hit Inception.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "Shaquille O'Neal appeared in the 1997 film Space Jam.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
    "question": "Ewan McGregor did not know the name of the second prequel film of Star Wars during and after filming.",
    "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "In Alfred Hitchcock's film Psycho, it is said he used chocolate syrup to simulate the blood in the famous shower scene",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "In the original Star Wars trilogy, David Prowse was the actor who physically portrayed Darth Vader.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "In the original Star Wars trilogy, Alec Guinness provided the voice for Darth Vader.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "Brandon Routh plays the titular character in the movie John Wick.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "George Lucas directed the entire original Star Wars trilogy.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "Actor Tommy Chong served prison time.", "correct_answer": "True",
     "incorrect_answers": ["False"]}
]



done = True
score = 0

questions_bank = [

]



for k in range(12):
    new_question = question_data[k]['question']
    new_answer = question_data[k]['correct_answer']
    questions_bank.append(Question(new_question,new_answer))


quiz = QuizBrain(questions_bank)


while quiz.still_has_quesitons():
    quiz.next_question()

print(f"Your final score is {quiz.score}/{quiz.question_number} ")
