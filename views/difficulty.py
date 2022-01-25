import pygame
import os
from .base import PygameView


class DifficultyView(PygameView):
    """Main view for the game - draws a rectangle on the screen"""

    def draw(self):
        # quiz image
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "img")
        self.window.fill((0, 0, 0))
        background = pygame.image.load(os.path.join(image_path, "quiz.png"))
        background = pygame.transform.scale(background, (300, 200))
        background_x = (500 - 300) / 2

        # difficulty rectangle
        pygame.draw.rect(self.window, (165, 102, 255), (50, 300, 100, 100))
        pygame.draw.rect(self.window, (128, 65, 217), (200, 300, 100, 100))
        pygame.draw.rect(self.window, (63, 0, 153), (350, 300, 100, 100))
        text1 = self.render_text_surface("EASY")
        text2 = self.render_text_surface("MIDIUM")
        text3 = self.render_text_surface("HARD")
        self.window.blit(background, (background_x, 70))
        self.window.blit(text1, (75, 333))
        self.window.blit(text2, (213, 333))
        self.window.blit(text3, (373, 333))
