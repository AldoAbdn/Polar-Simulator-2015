from Screens.Screen import Screen
from UI.Button import Button
import pygame

class StartMenu(Screen):
    def __init__(self, game) -> None:
        self.startButton = Button()
        super().__init__(pygame.image.load("assets/opening.jpg").convert(), [], [self.startButton], game)

    def handleUi(self):
        self.running = self.startButton.clicked()