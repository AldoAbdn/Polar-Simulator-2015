import pygame, sys
from Screens.StartMenu import StartMenu
from Screens.Fight import Fight
from Screens.GameOver import GameOver
from pygame.locals import *
pygame.init()

class Game:
    def __init__(self, fullscreen=True, fps=60) -> None:
        #Sets up display surface
        self.fullscreen = fullscreen
        self.surface = pygame.display.set_mode((1280, 720), FULLSCREEN|DOUBLEBUF|HWSURFACE)
        self.caption = "Polar simulator 2015"
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(pygame.image.load("../assets/player.png"))
        #Declaring Variables
        self.score = 0
        self.clock = pygame.time.Clock()
        self.time = 0.00
        self.fps = fps
        self.screens = [StartMenu(self), Fight(self), GameOver(self)]
        #Load main Music
        pygame.mixer.music.load("../assets/music.ogg")
        pygame.mixer.music.play(-1)

    #Runs game loop            
    def run(self):
        while True:
            for screen in self.screens:
                screen.preRun(self.score)
                while screen.running:
                    #Checks for events
                    self.handleEvents()
                    self.handleKeyPresses()
                    #Blit to Screen
                    screen.run()
                    #Update Display
                    pygame.display.flip()
                    #FPS
                    self.time = float(self.clock.tick_busy_loop(self.fps) / 1000.00)
                self.score += screen.score
                screen.reset()
            self.score = 0

    #Used to exit the game if x in pygame window is pressed
    def handleEvents(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()

    #Used to make game fullscreen using F key
    def handleKeyPresses(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[K_f]:
            #Tells python we mean the global fullscreen not a new local
            self.fullscreen = not self.fullscreen
            if self.fullscreen:
                pygame.display.set_mode((1280, 720), FULLSCREEN|DOUBLEBUF|HWSURFACE)
            else:
                pygame.display.set_mode((1280, 720), DOUBLEBUF|HWSURFACE)