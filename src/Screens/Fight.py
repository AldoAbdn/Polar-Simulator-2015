from Screen import Screen
import pygame

class Fight(Screen):
    def __init__(self, game) -> None:
        super().__init__(pygame.image.load("assets/background.jpg").convert(), sprites, ui, game)