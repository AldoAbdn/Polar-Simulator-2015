from Screens.Screen import Screen
from UI.Text import Text
import pygame, sys

class GameOver(Screen):
    def __init__(self, game) -> None:
        super().__init__("../assets/ending.jpg", [], [], game)

    def preRun(self, score):
        self.ui = [Text(640, 550, str(score), (255,0,0))]

    def handleKeyPresses(self):
        if self.game.keys[pygame.K_SPACE]:
            self.running = False
        elif self.game.keys[pygame.K_ESCAPE]:
            pygame.display.quit()
            sys.exit()  