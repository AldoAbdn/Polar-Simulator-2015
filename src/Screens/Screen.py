import pygame

class Screen:
    def __init__(self, background, sprites, ui) -> None:
        self.running = True
        self.background = pygame.image.load(background).convert()
        self.sprites = sprites
        self.ui = ui

    def run(self, surface):
        surface.blit(self.background, [0,0])
        self.draw()
        self.handleUi()
        self.handleSprites()
        pygame.display.flip()

    def draw(self):
        for ui in self.ui:
            ui.draw()
        for sprites in self.sprites:
            sprites.draw()

    def handleUi(self):
        pass

    def handleSprites(self):
        pass
    

        
    
        
