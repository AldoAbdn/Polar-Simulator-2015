from Screen import Screen
from UI.Text import Text
import pygame, sys

class GameOver(Screen):
    def __init__(self, game) -> None:
        background = pygame.image.load("assets/").convert()
        sprites = []
        ui = [Text()] 
        ui[0].updateText(str(self.game.score))
        super().__init__(background, sprites, ui, game)

    def handleKeyPresses(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.running = False
        elif keys[pygame.K_ESCAPE]:
            pygame.display.quit()
            sys.exit()  

        