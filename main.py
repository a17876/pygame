import pygame

from controllers import QuestionController, End, Difficulty
from views import QuestionView, EndView, DifficultyView
from models import Game, Question


# clock
# score calculation
# false - when user enter the answer


def main():
    """Main program"""

    # Initialize pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((500, 500))

    # Create the game view and controller
    difficulty_view = DifficultyView(window)
    difficulty = Difficulty(difficulty_view)

    # Run the game, stop after 10 seconds
    difficulty.run(stop_after=10)

    game = Game(difficulty = difficulty.difficulty, view= window)
    game.run()

    # Create the end view and controller, and run it
    end_view = EndView(view=window, score=game.score)
    end = End(end_view)
    end.run()

if __name__ == "__main__":
    main()
