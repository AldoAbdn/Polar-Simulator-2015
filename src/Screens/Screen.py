import pygame

class Screen:
    def __init__(self, background, sprites, ui, game) -> None:
        self.running = True
        self.background = pygame.image.load(background).convert()
        self.sprites = sprites
        self.ui = ui
        self.game = game

    def run(self):
        self.game.surface.blit(self.background, [0,0])
        self.draw()
        self.handleUi()
        self.handleSprites()
        self.handleEvents()
        self.handleKeyPresses()

    def draw(self):
        for ui in self.ui:
            ui.draw(self.game.surface)
        for sprites in self.sprites:
            sprites.move()
            sprites.draw(self.game.surface)

    def handleUi(self):
        pass

    def handleSprites(self):
        pass
    
    def handleEvents(self):
        pass

    def handleKeyPresses(self):
        pass

        
    
        
