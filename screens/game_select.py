import pygame
from pathlib import Path

class game_select:
    def __init__(self, app):
        pygame.init()

        self.screen = app.screen

        pygame.display.set_caption("Selection Screen - GameVault")

        self.width, self.length = self.screen.get_size()
        print(self.width,self.length)

        base_dir = Path(__file__).resolve().parent.parent
        data_dir = base_dir / "data"

        font_path = base_dir / "assets" / "PixelifySans-Regular.ttf"
        print(font_path.as_posix())

        self.button_font = pygame.font.Font(font_path, 40)

        self.running = True
