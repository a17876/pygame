from .base import PygameView


class EndView(PygameView):
    """View when the game is won"""

    def __init__(self, view, score):
        super().__init__(view)
        self.score = score


    def draw(self):
        self.window.fill((42, 0, 102))
        text = self.render_text_surface("Game ended.")
        self.window.blit(text, (185, 170))

        text = self.render_text_surface(f"Your score is: {self.score}")
        self.window.blit(text, (180, 250))




