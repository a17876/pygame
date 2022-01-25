import random
import requests
from html import unescape


class Question:
    def __init__(self, question, correct_answer, incorrect_answers):
        self.question = unescape(question)
        correct_answer = unescape(correct_answer)
        self.answers = [unescape(a) for a in incorrect_answers] + [correct_answer]
        random.shuffle(self.answers)
        self.answer_id = self.answers.index(correct_answer) + 1

    def get_answers(self):
        return "\n".join(
            [
                f"{idx+1}.  {answer}"
                for idx, answer in enumerate(self.answers)
            ]
        )

