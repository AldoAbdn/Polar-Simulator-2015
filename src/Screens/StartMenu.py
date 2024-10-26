from Screen import Screen
from UI.Button import Button
import pygame

class StartMenu(Screen):
    def __init__(self) -> None:
        self.background =  pygame.image.load("assets/opening.jpg").convert()
        self.sprites = []
        self.ui = [Button()]
        super().__init__(self.background, self.sprites, self.ui)

    def handleUi(self):
        self.running = self.ui[0].clicked()