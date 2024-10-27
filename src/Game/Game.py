import pygame, sys
from Screens.StartMenu import StartMenu
from Screens.Fight import Fight
from Screens.GameOver import GameOver
from pygame.locals import *
pygame.init()

class Game:
    def __init__(self, fullscreen=True, fps=60) -> None:
        self.fullscreen = fullscreen
        self.surface = pygame.display.set_mode((1280, 720), FULLSCREEN|DOUBLEBUF|HWSURFACE)
        #Sets up screen caption and icon
        self.caption = "Polar simulator 2015"
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(pygame.image.load("assets/player.png"))
        #Declaring Variables
        self.score = 0
        self.fpsClock = pygame.time.Clock()
        self.time = 0.00
        self.fps = fps
        self.screens = [StartMenu(self), Fight(self), GameOver(self)]
        #Load main Music
        pygame.mixer.music.load("assets/music.ogg")
        pygame.mixer.music.play(-1)

    #Runs game loop            
    def run(self):
        while True:
            for screen in self.screens:
                while screen.running:
                    #Checks for events and stores them in local variables
                    self.handleEvents()
                    self.handleKeyPresses()
                    #Blit to Screen
                    screen.run()
                    #Update Display
                    pygame.display.flip()
                    #FPS
                    self.time = float(self.fpsClock.Clock.tick_busy_loop(self.fps) / 1000.00)

    #Used to exit the game if x in pygame window is pressed
    def handleEvents(self):
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                running = False
                pygame.display.quit()
                sys.exit()

    #Used to make game fullscreen using F key
    def handleKeyPresses(self, key):
        keys = pygame.key.get_pressed()
        if key[K_f]:
            #Tells python we mean the global fullscreen not a new local
            self.fullscreen = not self.fullscreen
            if self.fullscreen:
                pygame.display.set_mode((1280, 720), FULLSCREEN|DOUBLEBUF|HWSURFACE)
            else:
                pygame.display.set_mode((1280, 720), DOUBLEBUF|HWSURFACE)