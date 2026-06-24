import pygame
from pathlib import Path

from screens.settings import Settings
from screens.game_select import game_select
#import repos
#import screens

class App:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
        pygame.display.set_caption("GameVault")

        self.width, self.length = self.screen.get_size()
        print(self.width,self.length)

        base_dir = Path(__file__).resolve().parent
        data_dir = base_dir / "data"

        font_path = base_dir / "assets" / "PixelifySans-Regular.ttf"
        print(font_path.as_posix())

        self.button_font = pygame.font.Font(font_path, 40)

        self.running = True
        

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            clock.tick(60)
            self.screen.fill((0, 0, 0))

            button_width = self.width  * 0.3
            button_length = self.length * 0.13
            Start_rect = pygame.rect.Rect(
                self.width // 2 - button_width //2,
                self.length // 3- button_length //3,
                button_width,
                button_length
            )

            pygame.draw.rect(self.screen, (255, 255, 255), Start_rect)
            text = self.button_font.render("Start", True, (0, 0, 0))
            text_rect = text.get_rect(center=Start_rect.center)
            self.screen.blit(text, text_rect)



            button_width = self.width  * 0.3
            button_length = self.length * 0.13
            Quit_rect = pygame.rect.Rect(
                self.width // 2 - button_width //2,
                self.length // 1.5- button_length //3,
                button_width,
                button_length
            )


            pygame.draw.rect(self.screen, (255, 255, 255), Quit_rect)
            text = self.button_font.render("Quit", True, (0, 0, 0))
            text_rect = text.get_rect(center=Quit_rect.center)
            self.screen.blit(text, text_rect)


            button_width = self.width  * 0.3
            button_length = self.length * 0.13
            Settings_rect = pygame.rect.Rect(
                self.width // 2 - button_width //2,
                self.length // 2- button_length //3,
                button_width,
                button_length
            )


            pygame.draw.rect(self.screen, (255, 255, 255), Settings_rect)
            text = self.button_font.render("Settings", True, (0, 0, 0))
            text_rect = text.get_rect(center=Settings_rect.center)
            self.screen.blit(text, text_rect)


            button_width = self.width  * 0.3
            button_length = self.length * 0.13
            button_rect = pygame.rect.Rect(
                self.width // 2 - button_width //2,
                self.length // 5- button_length //3,
                button_width,
                button_length
            )


            pygame.draw.rect(self.screen, (0, 0, 0), button_rect)
            text = self.button_font.render("GameVault", True, (255, 255, 255))
            text_rect = text.get_rect(center=button_rect.center)
            self.screen.blit(text, text_rect)


            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # left mouse click
                        if Quit_rect.collidepoint(event.pos):
                            print("Quit button clicked")
                            self.running = False

                        elif Settings_rect.collidepoint(event.pos):
                            print("Settings button clicked")
                            self.change_screen(Settings(self))

                        elif Start_rect.collidepoint(event.pos):
                            print("Start button clicked")
                            self.change_screen(game_select(self))
            
    def change_screen(self, new_screen):
        """Actionable method to transition screens"""
        self.current_screen = new_screen


if __name__ == "__main__":
    app = App()
    app.run()
