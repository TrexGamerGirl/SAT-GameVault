import pygame

class SettingsScreen:
    def __init__(self, app):
        self.app = app

    def draw(self, surface):
        surface.fill((50, 0, 50))

    def handle_event(self, event):
        pass