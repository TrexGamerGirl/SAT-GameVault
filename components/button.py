import pygame

class Button:
    def __init__(
            self,
            x,
            y,
            width,
            length,
            text,
            font,
            on_click=None,
            background_colour=(255,255,255),
            text_colour=(0,0,0)
    ):
        self.rect = pygame.Rect(x,y,width,length)
        self.text = text 
        self.font = font
        self.on_click = on_click
        self.background_colour = background_colour
        self.text_colour = text_colour

def draw(self, screen):
    pygame.draw.rect(screen, self.background_colour, self.rect)

    text_surface = self.font.renderer(
        self.text,
        True,
        self.text_colour
    )

    screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
        ):
            if self.rect.collidepoint(event.pos):
                if self.on_click:
                    self.on_click()