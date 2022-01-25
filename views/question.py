import pygame
from .base import PygameView
import os

class QuestionView(PygameView):
    """Main view for the game - draws a rectangle on the screen"""
    def __init__(self, view, question):
        super().__init__(view)
        self.question = question
        self.start = None
        
    def draw(self):
        # multilines of question and answers
        self.window.fill((0, 0, 0))
        answers = self.question.get_answers().split('\n')
        question_lst= self.question.question.split(' ')
        q_line1= ' '.join(question_lst[:7])
        q_line2=  ' '.join(question_lst[7:14])
        q_line3=  ' '.join(question_lst[14:])

        # background of question
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "img")
        q_img = pygame.image.load(os.path.join(image_path, "question.png"))
        q_img.set_colorkey((0, 0, 0))
        self.window.blit(q_img.convert(), (10, 50))

        # background of answers
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "img")
        answers_img = pygame.image.load(os.path.join(image_path, "answers.png"))
        answers_img.set_colorkey((0, 0, 0))
        answers_x = (500 - 400) / 2
        self.window.blit(answers_img.convert(), (answers_x, 250))

        # render the question
        q_line1 = self.render_text_surface(q_line1)
        self.window.blit(q_line1, (30, 80))
        q_line2 = self.render_text_surface(q_line2)
        self.window.blit(q_line2, (30, 110))
        q_line3 = self.render_text_surface(q_line3)
        self.window.blit(q_line3, (30, 140))

        # render the answers
        an1 = self.render_text_surface(answers[0])
        self.window.blit(an1 , (60, 270))
        an2  = self.render_text_surface(answers[1])
        self.window.blit(an2 , (60, 310))
        an3  = self.render_text_surface(answers[2])
        self.window.blit(an3 , (60, 350))
        an4  = self.render_text_surface(answers[3])
        self.window.blit(an4 , (60, 390))
        
        # render the time left
        now =  pygame.time.get_ticks()
        timer = self.render_text_surface(str(10- int((now - self.start)/1000)))
        self.window.blit(timer, (450, 10))