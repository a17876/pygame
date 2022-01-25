import pygame.locals

from .base import PygameController


class Difficulty(PygameController):
    """Main game controller"""

    def __init__(self, view):
        """Constructor - sets variables"""
        super().__init__(view)
        self.difficulty = ''

    def process(self, event):
        """
        This method overrides the parent's.
        Its job is to do something when the user clicks in the shape.
        """

        # First call the parent method, just in case we want to exit
        running = super().process(event)

        if running is False:
            return False

        if event.type == pygame.locals.MOUSEBUTTONDOWN:
            # Check the click position, and register the number of clicks
            if 50 <= event.pos[0] <= 150 and 300 <= event.pos[1] <= 400:
                self.difficulty = "easy"
            elif 200 <= event.pos[0] <= 300 and 300 <= event.pos[1] <= 400:
                self.difficulty = "medium"
            elif 350 <= event.pos[0] <= 450 and 300 <= event.pos[1] <= 400:
                self.difficulty = "hard"

            print(self.difficulty)
            return False

        return True