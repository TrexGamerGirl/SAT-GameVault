import pygame
from pathlib import Path

#import repos
#import screens

class App:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((750, 460),pygame.RESIZABLE)
        pygame.display.set_caption("GameVault")

        base_dir = Path(__file__).resolve().parent
        data_dir = base_dir / "data"

        self.running = True

    def run(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((30, 30, 30))

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.run()
