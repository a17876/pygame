import requests

from controllers import QuestionController
from views import QuestionView
from .question import Question

class Game:
    def __init__(self, difficulty, view, num=3, ):
        stuff = requests.get("https://opentdb.com/api.php?amount=" + str(num) + "&type=multiple&category=9&difficulty=" + difficulty).json()
        self.questions = [
            Question(
                elem["question"],
                elem["correct_answer"],
                elem["incorrect_answers"],
            )
            for elem in stuff["results"]
        ]
        self.score = 0
        self.difficulty = difficulty
        self.window = view

    def run(self):
        for item in self.questions:
            print(item.answer_id)
            question_view = QuestionView(self.window, item)
            question = QuestionController(question_view, item)
            question.run(stop_after=3)
            self.score += question.score
    
            
