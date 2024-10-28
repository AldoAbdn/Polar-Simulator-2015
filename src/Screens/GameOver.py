from Screens.Screen import Screen
from UI.Text import Text
import pygame, sys

class GameOver(Screen):
    def __init__(self, game) -> None:
        ui = [Text(500, 640, str(game.score), (255,0,0))]
        super().__init__("../assets/ending.jpg", [], ui, game)

    def handleKeyPresses(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.running = False
        elif keys[pygame.K_ESCAPE]:
            pygame.display.quit()
            sys.exit()  

        