import pygame.locals

from .base import PygameController

class QuestionController(PygameController):
    """Main game controller"""

    def __init__(self, view, question):
        """Constructor - sets variables"""
        super().__init__(view)
        self.score = 0
        self.question = question
        self.user_answer = ''

    def process(self, event):
        """
        This method overrides the parent's.
        Its job is to do something when the user clicks in the shape.
        """     
        # First call the parent method, just in case we want to exit
        running = super().process(event)
        
        if running is False:
            return False
        
        if event.type == pygame.locals.KEYDOWN:
            # Save the key value that user enter
            if event.key == pygame.locals.K_1:
                self.user_answer = 1
            elif event.key == pygame.locals.K_2:
                self.user_answer = 2
            elif event.key == pygame.locals.K_3:
                self.user_answer = 3
            elif event.key == pygame.locals.K_4:
                self.user_answer = 4

            print(f'user:{self.user_answer}')

            
            if str(self.question.answer_id) == str(self.user_answer):
                self.score += 1 
                print(f'score:{self.score}')
            # else:
            #     self.score = self.score
            #     print(f'score:{self.score}')

            return False


        return True

    def run(self, stop_after):
        now = pygame.time.get_ticks()
        self.view.start = now
        super().run(stop_after)
