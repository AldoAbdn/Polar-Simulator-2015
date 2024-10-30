from Screens.Screen import Screen
from UI.Text import Text
import pygame, sys

class GameOver(Screen):
    def __init__(self, game) -> None:
        ui = [Text(640, 550, str(game.score), (255,0,0))]
        super().__init__("../assets/ending.jpg", [], ui, game)

    def handleKeyPresses(self):
        if self.game.keys[pygame.K_SPACE]:
            self.running = False
        elif self.game.keys[pygame.K_ESCAPE]:
            pygame.display.quit()
            sys.exit()  

        