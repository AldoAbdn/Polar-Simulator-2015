from Screens.Screen import Screen
from UI.Button import Button
import pygame

class StartMenu(Screen):
    def __init__(self, game) -> None:
        self.startButton = Button(640, 640, "START", (0,0,0), (255,0,0))
        super().__init__("../assets/opening.jpg", [], [self.startButton], game)

    def handleUi(self):
        self.running = self.startButton.clicked()